# -*- encoding: utf-8 -*-
from abjad import *


def test_Spanner_pop_left_01():
    r'''Remove and return leftmost component in spanner.
    '''

    voice = Voice(Container(notetools.make_repeated_notes(2)) * 3)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(voice)
    beam = spannertools.BeamSpanner(voice[:])

    r'''
    \new Voice {
        {
            c'8 [
            d'8
        }
        {
            e'8
            f'8
        }
        {
            g'8
            a'8 ]
        }
    }
    '''

    result = beam.pop_left()

    r'''
    \new Voice {
        {
            c'8
            d'8
        }
        {
            e'8 [
            f'8
        }
        {
            g'8
            a'8 ]
        }
    }
    '''

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            {
                c'8
                d'8
            }
            {
                e'8 [
                f'8
            }
            {
                g'8
                a'8 ]
            }
        }
        '''
        )
    assert result is voice[0]
