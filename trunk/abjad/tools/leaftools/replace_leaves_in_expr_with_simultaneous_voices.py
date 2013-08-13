# -*- encoding: utf-8 -*-
import copy
import itertools
from abjad.tools import selectiontools


def replace_leaves_in_expr_with_simultaneous_voices(expr):
    r'''Replace leaves in `expr` with two simultaneous voices containing copies of
    leaves in `expr`:

    ::

        >>> c = p('{ c c c c }')
        >>> f(c)
        {
            c4
            c4
            c4
            c4
        }

    ::

        >>> leaftools.replace_leaves_in_expr_with_simultaneous_voices(c.select_leaves()[1:3])
        ([Note('c4'), Note('c4')], [Note('c4'), Note('c4')])

    ..  doctest::

        >>> f(c)
        {
            c4
            <<
                \new Voice {
                    c4
                    c4
                }
                \new Voice {
                    c4
                    c4
                }
            >>
            c4
        }

    If leaves in `expr` have different immediate parents, simultaneous voices will
    be created in each parent:

    ::

        >>> c = p(r'{ c8 \times 2/3 { c8 c c } \times 4/5 { c16 c c c c } c8 }')
        >>> f(c)
        {
            c8
            \times 2/3 {
                c8
                c8
                c8
            }
            \times 4/5 {
                c16
                c16
                c16
                c16
                c16
            }
            c8
        }

    ::

        >>> leaves = leaftools.replace_leaves_in_expr_with_simultaneous_voices(c.select_leaves()[2:7])

    ..  doctest::

        >>> f(c)
        {
            c8
            \times 2/3 {
                c8
                <<
                    \new Voice {
                        c8
                        c8
                    }
                    \new Voice {
                        c8
                        c8
                    }
                >>
            }
            \times 4/5 {
                <<
                    \new Voice {
                        c16
                        c16
                        c16
                    }
                    \new Voice {
                        c16
                        c16
                        c16
                    }
                >>
                c16
                c16
            }
            c8
        }

    Returns a list leaves in upper voice, and a list of leaves in lower voice.
    '''
    from abjad.tools import componenttools
    from abjad.tools import containertools
    from abjad.tools import iterationtools
    from abjad.tools import spannertools
    from abjad.tools import voicetools

    leaves = [leaf for leaf in iterationtools.iterate_leaves_in_expr(expr)]

    upper_leaves = []
    lower_leaves = []

    for parent, group in itertools.groupby(leaves, lambda x: x._parent):
        grouped_leaves = list(group)
        grouped_leaves = selectiontools.ContiguousSelection(grouped_leaves)
        start_idx = parent.index(grouped_leaves[0])
        stop_idx = parent.index(grouped_leaves[-1])

        container = containertools.Container()
        container.is_simultaneous = True
        new_leaves = grouped_leaves.copy_and_fracture_crossing_spanners()
        spannertools.detach_spanners_attached_to_components_in_expr(new_leaves)
        upper_voice = voicetools.Voice(new_leaves)
        new_leaves = grouped_leaves.copy_and_fracture_crossing_spanners()
        spannertools.detach_spanners_attached_to_components_in_expr(new_leaves)
        lower_voice = voicetools.Voice(new_leaves)

        container.extend([upper_voice, lower_voice])

        upper_leaves.extend(upper_voice[:])
        lower_leaves.extend(lower_voice[:])

        parent[start_idx:stop_idx+1] = [container]

    return upper_leaves, lower_leaves