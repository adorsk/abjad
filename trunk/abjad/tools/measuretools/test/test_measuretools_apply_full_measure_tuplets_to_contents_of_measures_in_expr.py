# -*- encoding: utf-8 -*-
from abjad import *


def test_measuretools_apply_full_measure_tuplets_to_contents_of_measures_in_expr_01():

    staff = Staff([Measure((2, 8), "c'8 d'8"), Measure((3, 8), "e'8 f'8 g'8")])

    r'''
    \new Staff {
        {
            \time 2/8
            c'8
            d'8
        }
        {
            \time 3/8
            e'8
            f'8
            g'8
        }
    }
    '''

    measuretools.apply_full_measure_tuplets_to_contents_of_measures_in_expr(staff)

    r'''
    \new Staff {
        {
            \time 2/8
            {
                c'8
                d'8
            }
        }
        {
            \time 3/8
            {
                e'8
                f'8
                g'8
            }
        }
    }
    '''

    assert select(staff).is_well_formed()
    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 2/8
                {
                    c'8
                    d'8
                }
            }
            {
                \time 3/8
                {
                    e'8
                    f'8
                    g'8
                }
            }
        }
        '''
        )
