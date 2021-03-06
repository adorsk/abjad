# -*- encoding: utf-8 -*-
from abjad.tools import indicatortools
from abjad.tools import scoretools
from abjad.tools import stringtools
from abjad.tools.spannertools.Spanner import Spanner


class Hairpin(Spanner):
    r'''A hairpin.

    ..  container:: example

        ::

            >>> staff = Staff("r4 c'8 d'8 e'8 f'8 r4")
            >>> hairpin = spannertools.Hairpin(
            ...     descriptor='p < f',
            ...     include_rests=False,
            ...     )
            >>> attach(hairpin, staff[:])
            >>> show(staff) # doctest: +SKIP

        ..  doctest::

            >>> print format(staff)
            \new Staff {
                r4
                c'8 \< \p
                d'8
                e'8
                f'8 \f
                r4
            }

    '''

    ### CLASS VARIABLES ###

    _hairpin_shape_strings = (
        '<',
        '>',
        )

    __slots__ = (
        '_descriptor',
        '_direction',
        '_include_rests',
        '_shape_string',
        '_start_dynamic',
        '_stop_dynamic',
        )

    ### INITIALIZER ###

    def __init__(
        self,
        descriptor='<',
        direction=None,
        include_rests=False,
        overrides=None,
        ):
        Spanner.__init__(
            self,
            overrides=overrides,
            )
        direction = stringtools.arg_to_tridirectional_lilypond_symbol(
            direction)
        self._direction = direction
        self._include_rests = include_rests
        start_dynamic, shape_string, stop_dynamic = \
            self._parse_descriptor(descriptor)
        self._descriptor = descriptor
        assert shape_string in ('<', '>')
        self._shape_string = shape_string
        if start_dynamic is not None:
            start_dynamic = indicatortools.Dynamic(start_dynamic)
        self._start_dynamic = start_dynamic
        if stop_dynamic is not None:
            stop_dynamic = indicatortools.Dynamic(stop_dynamic)
        self._stop_dynamic = stop_dynamic

    ### PRIVATE METHODS ###

    def _copy_keyword_args(self, new):
        #Spanner._copy_keyword_args(self, new)
        new._direction = self.direction
        new._include_rests = self.include_rests
        new._shape_string = self.shape_string
        new._start_dynamic = self.start_dynamic
        new._stop_dynamic = self.stop_dynamic

    def _format_right_of_leaf(self, leaf):
        result = []
        direction_string = ''
        if self.direction is not None:
            direction_string = \
                stringtools.arg_to_tridirectional_lilypond_symbol(
                    self.direction)
            direction_string = '{} '.format(direction_string)
        if self.include_rests:
            if self._is_my_first_leaf(leaf):
                string = '{}\\{}'.format(direction_string, self.shape_string)
                result.append(string)
                if self.start_dynamic:
                    string = '{}\\{}'.format(
                        direction_string, 
                        self.start_dynamic.name,
                        )
                    result.append(string)
            if self._is_my_last_leaf(leaf):
                if self.stop_dynamic:
                    string = '{}\\{}'.format(
                        direction_string,
                        self.stop_dynamic.name,
                        )
                    result.append(string)
                else:
                    effective_dynamic = leaf._get_effective(
                        indicatortools.Dynamic)
                    if effective_dynamic is None:
                        result.append('\\!')
                    elif effective_dynamic not in leaf._indicators:
                        found_match = False
                        for indicator in \
                            leaf._get_indicators(indicatortools.Dynamic):
                            if indicator == effective_dynamic:
                                found_match = True
                        if not found_match:
                            result.append('\\!')
        else:
            if self._is_my_first(leaf, (scoretools.Chord, scoretools.Note)):
                string = '{}\\{}'.format(
                    direction_string, 
                    self.shape_string,
                    )
                result.append(string)
                if self.start_dynamic:
                    string = '{}\\{}'.format(
                        direction_string, 
                        self.start_dynamic.name,
                        )
                    result.append(string)
            if self._is_my_last(leaf, (scoretools.Chord, scoretools.Note)):
                if self.stop_dynamic:
                    string = '{}\\{}'.format(
                        direction_string, 
                        self.stop_dynamic.name,
                        )
                    result.append(string)
                else:
                    effective_dynamic = leaf._get_effective(
                        indicatortools.Dynamic)
                    if effective_dynamic is None:
                        result.append('\\!')
        return result

    @staticmethod
    def _is_hairpin_shape_string(arg):
        return arg in Hairpin._hairpin_shape_strings

    @staticmethod
    def _is_hairpin_token(arg):
        r'''Is true when `arg` is a hairpin token. Otherwise false:

        ::

            >>> spannertools.Hairpin._is_hairpin_token(('p', '<', 'f'))
            True

        ::

            >>> spannertools.Hairpin._is_hairpin_token(('f', '<', 'p'))
            False

        Returns boolean.
        '''
        Dynamic = indicatortools.Dynamic
        if isinstance(arg, tuple) and \
            len(arg) == 3 and \
            (not arg[0] or indicatortools.Dynamic.is_dynamic_name(arg[0])) \
            and Hairpin._is_hairpin_shape_string(arg[1]) and \
            (not arg[2] or indicatortools.Dynamic.is_dynamic_name(arg[2])):
            if arg[0] and arg[2]:
                start_ordinal = \
                    Dynamic.dynamic_name_to_dynamic_ordinal(arg[0])
                stop_ordinal = \
                    Dynamic.dynamic_name_to_dynamic_ordinal(arg[2])
                if arg[1] == '<':
                    return start_ordinal < stop_ordinal
                else:
                    return stop_ordinal < start_ordinal
            else:
                return True
        else:
            return False

    def _parse_descriptor(self, descriptor):
        r'''Example descriptors:

        ::

            '<'
            'p <'
            'p < f'

        '''
        assert isinstance(descriptor, str)
        parts = descriptor.split()
        num_parts = len(parts)
        start, shape, stop = None, None, None
        if parts[0] in ('<', '>'):
            assert 1 <= num_parts <= 2
            if num_parts == 1:
                shape = parts[0]
            else:
                shape = parts[0]
                stop = parts[1]
        else:
            assert 2 <= num_parts <= 3
            if num_parts == 2:
                start = parts[0]
                shape = parts[1]
            else:
                start = parts[0]
                shape = parts[1]
                stop = parts[2]
        assert shape in ('<', '>')
        return start, shape, stop

    ### PUBLIC PROPERTIES ###

    @property
    def descriptor(self):
        r'''Gets descriptor of hairpin.

        ..  container:: example

            ::

                >>> staff = Staff("r4 c'8 d'8 e'8 f'8 r4")
                >>> hairpin = spannertools.Hairpin(descriptor='p < f')
                >>> attach(hairpin, staff[:])
                >>> show(staff) # doctest: +SKIP

            ::

                >>> hairpin.descriptor
                'p < f'

        Returns string.
        '''
        return self._descriptor

    @property
    def direction(self):
        r'''Gets direction of hairpin.

        ..  container:: example

            Positions hairpin above staff:

            ::

                >>> staff = Staff("r4 c'8 d'8 e'8 f'8 r4")
                >>> hairpin = spannertools.Hairpin(
                ...     descriptor='p < f',
                ...     direction=Up,
                ...     )
                >>> attach(hairpin, staff[:])
                >>> show(staff) # doctest: +SKIP

        ..  doctest::

            >>> print format(staff)
            \new Staff {
                r4
                c'8 ^ \< ^ \p
                d'8
                e'8
                f'8 ^ \f
                r4
            }

            ::

                >>> hairpin.direction
                '^'

        Returns up, down or none.
        '''
        return self._direction

    @property
    def include_rests(self):
        r'''Gets include-rests flag of hairpin.

        ..  container:: example

            ::

                >>> staff = Staff("r4 c'8 d'8 e'8 f'8 r4")
                >>> hairpin = spannertools.Hairpin(
                ...     descriptor='p < f',
                ...     include_rests=True,
                ...     )
                >>> attach(hairpin, staff[:])
                >>> show(staff) # doctest: +SKIP

        ..  doctest::

            >>> print format(staff)
            \new Staff {
                r4 \< \p
                c'8
                d'8
                e'8
                f'8
                r4 \f
            }

            ::

                >>> hairpin.include_rests
                True

        Returns boolean.
        '''
        return self._include_rests

    @property
    def shape_string(self):
        r'''Gets shape string of hairpin.

        ..  container:: example

            ::

                >>> staff = Staff("r4 c'8 d'8 e'8 f'8 r4")
                >>> hairpin = spannertools.Hairpin(descriptor='p < f')
                >>> attach(hairpin, staff[:])
                >>> show(staff) # doctest: +SKIP

            ::

                >>> hairpin.shape_string
                '<'

        Returns string.
        '''
        return self._shape_string

    @property
    def start_dynamic(self):
        r'''Gets start dynamic string of hairpin.

        ..  container:: example

            ::

                >>> staff = Staff("r4 c'8 d'8 e'8 f'8 r4")
                >>> hairpin = spannertools.Hairpin(descriptor='p < f')
                >>> attach(hairpin, staff[:])
                >>> show(staff) # doctest: +SKIP

            ::

                >>> hairpin.start_dynamic
                Dynamic(name='p')

        Returns dynamic or none.
        '''
        return self._start_dynamic

    @property
    def stop_dynamic(self):
        r'''Gets stop dynamic string of hairpin.

        ..  container:: example

            ::

                >>> staff = Staff("r4 c'8 d'8 e'8 f'8 r4")
                >>> hairpin = spannertools.Hairpin(descriptor='p < f')
                >>> attach(hairpin, staff[:])
                >>> show(staff) # doctest: +SKIP

            ::

                >>> hairpin.stop_dynamic
                Dynamic(name='f')

        Returns dynamic or none.
        '''
        return self._stop_dynamic
