# -*- encoding: utf-8 -*-
from abjad import *


def test_scoretools_fill_measures_in_expr_with_time_signature_denominator_notes_01():
    r'''Populate non-power-of-two measure with time signature denominator notes.
    '''

    measure = Measure((5, 18), [])
    scoretools.fill_measures_in_expr_with_time_signature_denominator_notes(measure)

    r'''
    {
        \time 5/18
        \scaleDurations #'(8 . 9) {
            c'16
            c'16
            c'16
            c'16
            c'16
        }
    }
    '''

    assert inspect(measure).is_well_formed()
    assert systemtools.TestManager.compare(
        measure,
        r'''
        {
            \time 5/18
            \scaleDurations #'(8 . 9) {
                c'16
                c'16
                c'16
                c'16
                c'16
            }
        }
        '''
        )
