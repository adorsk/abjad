# -*- encoding: utf-8 -*-
from abjad.tools import sequencetools
from abjad.tools.pitchtools.PitchClassSet import PitchClassSet


class  NumberedPitchClassSet(PitchClassSet):
    '''Abjad model of a numbered chromatic pitch-class set:

    ::

        >>> ncpcs = pitchtools.NumberedPitchClassSet(
        ...     [-2, -1.5, 6, 7, -1.5, 7])

    ::

        >>> ncpcs
        NumberedPitchClassSet([6, 7, 10, 10.5])

    ::

        >>> print ncpcs
        {6, 7, 10, 10.5}

    Numbered chromatic pitch-class sets are immutable.
    '''

    ### CLASS VARIABLES ###

    __slots__ = (
        )

    ### CONSTRUCTOR ###

    def __new__(cls, expr):
        from abjad.tools import pitchtools
        pcs = []
        # assume expr is iterable
        try:
            for x in expr:
                try:
                    pcs.append(pitchtools.NumberedPitchClass(x))
                except TypeError:
                    pcs.extend(pitchtools.get_numbered_chromatic_pitch_classes_from_pitch_carrier(x))
        # if expr is not iterable
        except TypeError:
            # assume expr can be turned into a single pc
            try:
                pc = pitchtools.NumberedPitchClass(expr)
                pcs.append(pc)
            # expr is a Rest or non-PC type
            except TypeError:
                pcs = []
        return frozenset.__new__(cls, pcs)

    ### SPECIAL METHODS ###

    def __eq__(self, arg):
        if isinstance(arg, type(self)):
            for element in arg:
                if element not in self:
                    return False
            else:
                return True
        return False

    def __hash__(self):
        return hash(repr(self))

    def __ne__(self, arg):
        return not self == arg

    def __repr__(self):
        return '%s([%s])' % (self._class_name, self._format_string)

    def __str__(self):
        return '{%s}' % self._format_string

    ### PRIVATE PROPERTIES ###

    @property
    def _format_string(self):
        result = list(self)
        result.sort(key=lambda x: abs(x))
        return ', '.join([str(x) for x in result])

    ### PUBLIC PROPERTIES ###

    @property
    def inversion_equivalent_chromatic_interval_class_set(self):
        r'''Inversion-equivalent chromatic interval-class set:

        ::

            >>> ncpcs.inversion_equivalent_chromatic_interval_class_set
            NumberedInversionEquivalentIntervalClassSet(0.5, 1, 3, 3.5, 4, 4.5)

        Return inversion-equivalent chromatic interval-class set.
        '''
        from abjad.tools import pitchtools
        interval_class_set = set([])
        for first_pc, second_pc in \
            sequencetools.yield_all_unordered_pairs_of_sequence(self):
            interval_class = first_pc - second_pc
            interval_class_set.add(interval_class)
        interval_class_set = \
            pitchtools.NumberedInversionEquivalentIntervalClassSet(
            interval_class_set)
        return interval_class_set

    @property
    def inversion_equivalent_chromatic_interval_class_vector(self):
        r'''Inversion-equivalent chromatic interval-class vector:

        ::

            >>> ncpcs.inversion_equivalent_chromatic_interval_class_vector
            NumberedInversionEquivalentIntervalClassVector(0 | 1 0 1 1 0 0 1 0 0 1 1 0)

        Return inversion-equivalent chromatic interval-class vector.
        '''
        from abjad.tools import pitchtools
        interval_classes = []
        for first_pc, second_pc in \
            sequencetools.yield_all_unordered_pairs_of_sequence(self):
            interval_class = first_pc - second_pc
            interval_classes.append(interval_class)
        return pitchtools.NumberedInversionEquivalentIntervalClassVector(
            interval_classes)

    @property
    def numbered_chromatic_pitch_classes(self):
        r'''Numbered chromatic pitch-classes:

        ::

            >>> result = ncpcs.numbered_chromatic_pitch_classes

        ::

            >>> for x in result: x
            ...
            NumberedPitchClass(6)
            NumberedPitchClass(7)
            NumberedPitchClass(10)
            NumberedPitchClass(10.5)

        Return tuple.
        '''
        result = list(self)
        result.sort(key=lambda x: abs(x))
        return tuple(result)

    @property
    def prime_form(self):
        r'''To be implemented.
        '''
        return None

    ### PUBLIC METHODS ###

    def invert(self):
        r'''Invert numbered chromatic pitch-class set:

        ::

            >>> ncpcs.invert()
            NumberedPitchClassSet([1.5, 2, 5, 6])

        Return numbered chromatic pitch-class set.
        '''
        return type(self)([pc.invert() for pc in self])

    def is_transposed_subset(self, pcset):
        r'''True when self is transposed subset of `pcset`.
        False otherwise:

        ::

            >>> pcset_1 = pitchtools.NumberedPitchClassSet(
            ... [-2, -1.5, 6, 7, -1.5, 7])
            >>> pcset_2 = pitchtools.NumberedPitchClassSet(
            ... [-2, -1.5, 6, 7, -1.5, 7, 7.5, 8])

        ::

            >>> pcset_1.is_transposed_subset(pcset_2)
            True

        Return boolean.
        '''
        for n in range(12):
            if self.transpose(n).issubset(pcset):
                return True
        return False

    def is_transposed_superset(self, pcset):
        r'''True when self is transposed superset of `pcset`.
        False otherwise:

        ::

            >>> pcset_1 = pitchtools.NumberedPitchClassSet(
            ... [-2, -1.5, 6, 7, -1.5, 7])
            >>> pcset_2 = pitchtools.NumberedPitchClassSet(
            ... [-2, -1.5, 6, 7, -1.5, 7, 7.5, 8])

        ::

            >>> pcset_2.is_transposed_superset(pcset_1)
            True

        Return boolean.
        '''
        for n in range(12):
            if self.transpose(n).issuperset(pcset):
                return True
        return False

    def multiply(self, n):
        r'''Multiply numbered chromatic pitch-class set by `n`:

        ::

            >>> ncpcs.multiply(5)
            NumberedPitchClassSet([2, 4.5, 6, 11])

        Return numbered chromatic pitch-class set.
        '''
        return type(self)([pc.multiply(n) for pc in self])

    def transpose(self, n):
        r'''Transpose numbered chromatic pitch-class set by `n`:

        ::

            >>> ncpcs.transpose(5)
            NumberedPitchClassSet([0, 3, 3.5, 11])

        Return numbered chromatic pitch-class set.
        '''
        return type(self)([pc.transpose(n) for pc in self])