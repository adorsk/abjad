# -*- encoding: utf-8 -*-
from abjad import *


def test_scoretools_Measure_time_signature_update_01():
    r'''Measures allow time signature update.
    '''

    measure = Measure((4, 8), "c'8 d'8 e'8 f'8")
    measure.pop()
    inspect(measure).get_mark(marktools.TimeSignatureMark).detach()
    time_signature = marktools.TimeSignatureMark((3, 8))
    attach(time_signature, measure)

    assert testtools.compare(
        measure,
        r'''
        {
            \time 3/8
            c'8
            d'8
            e'8
        }
        '''
        )

    assert inspect(measure).is_well_formed()