# -*- encoding: utf-8 -*-
from abjad import *


def test_NaturalHarmonic___init___01():
    r'''Init natural harmonic from note.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    natural_harmonic = notetools.NaturalHarmonic(staff[1])
    componenttools.move_parentage_and_spanners_from_components_to_components(staff[1:2], [natural_harmonic])

    r'''
    \new Staff {
        c'8
        \once \override NoteHead #'style = #'harmonic
        d'8
        e'8
        f'8
    }
    '''

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            c'8
            \once \override NoteHead #'style = #'harmonic
            d'8
            e'8
            f'8
        }
        '''
        )
