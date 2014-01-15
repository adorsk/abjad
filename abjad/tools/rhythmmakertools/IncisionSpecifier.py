# -*- encoding: utf-8 -*-
from abjad.tools.abctools import AbjadObject


class IncisionSpecifier(AbjadObject):
    r'''Incision specifier.
    '''

    ### INITIALIZER ###

    def __init__(
        self,
        prefix_talea=(8,),
        prefix_lengths=(1, 2, 3, 4),
        suffix_talea=(1,),
        suffix_lengths=(1,),
        talea_denominator=32,
        ):
        prefix_talea = self._to_tuple(prefix_talea)
        assert prefix_talea is None or \
            sequencetools.all_are_integer_equivalent_numbers(
            prefix_talea), prefix_talea
        self._prefix_talea = prefix_talea
        prefix_lengths = self._to_tuple(prefix_lengths)
        assert prefix_lengths is None or \
            sequencetools.all_are_nonnegative_integer_equivalent_numbers(
            prefix_lengths), prefix_lengths
        self._prefix_lengths = prefix_lengths
        suffix_talea = self._to_tuple(suffix_talea)
        assert suffix_talea is None or \
            sequencetools.all_are_integer_equivalent_numbers(
            suffix_talea), suffix_talea
        self._suffix_talea = suffix_talea
        suffix_lengths = self._to_tuple(suffix_lengths)
        assert suffix_lengths is None or \
            sequencetools.all_are_nonnegative_integer_equivalent_numbers(
            suffix_lengths), suffix_lengths
        self._suffix_lengths = suffix_lengths
        assert mathtools.is_positive_integer_equivalent_number(
            talea_denominator), talea_denominator
        self._talea_denominator = talea_denominator

    ### PRIVATE METHODS ###

    @staticmethod
    def _to_tuple(expr):
        if isinstance(expr, list):
            expr = tuple(expr)
        return expr

    ### PUBLIC PROPERTIES ###

    @property
    def prefix_lengths(self):
        r'''Gets prefix lengths of incision specifier.

        Returns tuple or none.
        '''
        return self._prefix_lengths

    @property
    def prefix_talea(self):
        r'''Gets prefix talea of incision specifier.

        Returns tuple or none.
        '''
        return self._prefix_talea

    @property
    def suffix_lengths(self):
        r'''Gets suffix lengths of incision specifier.

        Returns tuple or none.
        '''
        return self._suffix_lenghts

    @property
    def suffix_talea(self):
        r'''Gets suffix talea of incision specifier.

        Returns tuple or none.
        '''
        return self._suffix_lenghts

    @property
    def talea_denominator(self):
        r'''Gets talea denominator of incision specifier.

        Returns positive integer-equivalent number.
        '''
        return self._talea_denominator
