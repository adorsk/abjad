# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import componenttools
from abjad.tools import contexttools
from abjad.tools import mathtools


def pad_measures_in_expr(expr, front, back, pad_class, splice=False):
    r'''Pad measures in `expr`.
    '''
    from abjad.tools import iterationtools
    from abjad.tools import leaftools
    from abjad.tools import resttools
    from abjad.tools import skiptools

    if not isinstance(front, (durationtools.Duration, type(None))):
        raise ValueError

    if not isinstance(back, (durationtools.Duration, type(None))):
        raise ValueError

    if not isinstance(pad_class, (resttools.Rest, skiptools.Skip)):
        raise TypeError

    root = expr[0]._get_parentage().root

    # TODO: maybe create ForbidUpdates context manager?
    # forbid updates because self._splice() calls self.stop_offset
    root._update_now(offsets=True)
    root._is_forbidden_to_update = True

    for measure in iterationtools.iterate_measures_in_expr(expr):
        if front is not None:
            start_components = measure._get_descendants_starting_with()
            start_leaves = \
                [x for x in start_components if isinstance(x, leaftools.Leaf)]
            for start_leaf in start_leaves:
                if splice:
                    start_leaf._splice(
                        [pad_class.__class__(front)], 
                        direction=Left,
                        grow_spanners=True,
                        )
                else:
                    start_leaf._splice(
                        [pad_class.__class__(front)], 
                        direction=Left,
                        grow_spanners=False,
                        )
        if back is not None:
            stop_components = measure._get_descendants_stopping_with()
            stop_leaves = \
                [x for x in stop_components if isinstance(x, leaftools.Leaf)]
            for stop_leaf in stop_leaves:
                if splice:
                    stop_leaf._splice(
                        [pad_class.__class__(back)],
                        grow_spanners=True,
                        )
                else:
                    stop_leaf._splice(
                        [pad_class.__class__(back)],
                        grow_spanners=False,
                        )
        if front is not None or back is not None:
            new_duration = measure._get_duration()
            new_time_signature = mathtools.NonreducedFraction(new_duration)
            old_time_signature = measure._get_mark(
                contexttools.TimeSignatureMark)
            new_time_signature = new_time_signature.with_denominator(
                old_time_signature.denominator)
            new_time_signature = contexttools.TimeSignatureMark(
                new_time_signature)
            for mark in measure._get_marks(contexttools.TimeSignatureMark):
                mark.detach()
            new_time_signature.attach(measure)

    # allow updates after all calls to spanner-growing functions are done
    root._update_later(offsets=True)
    root._is_forbidden_to_update = False
