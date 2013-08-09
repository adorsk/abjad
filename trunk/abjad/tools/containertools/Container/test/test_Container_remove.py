# -*- encoding: utf-8 -*-
from abjad import *
import py.test


def test_Container_remove_01():
    r'''Containers remove leaves correctly.
    Leaf detaches from parentage.
    Leaf withdraws from crossing spanners.
    Leaf carries covered spanners forward.
    Leaf returns after removal.
    '''

    voice = Voice("c'8 d'8 e'8 f'8")
    spannertools.SlurSpanner(voice[:])
    spannertools.BeamSpanner(voice[1])

    r'''
    \new Voice {
        c'8 (
        d'8 [ ]
        e'8
        f'8 )
    }
    '''

    #result = voice.remove(voice[1])
    note = voice[1]
    voice.remove(note)

    r'''
    \new Voice {
        c'8 (
        e'8
        f'8 )
    }
    '''

    assert select(voice).is_well_formed()
    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            c'8 (
            e'8
            f'8 )
        }
        '''
        )

    "Note is now d'8 [ ]"

    #assert select(result).is_well_formed()
    assert select(note).is_well_formed()
    #assert result.lilypond_format == "d'8 [ ]"
    assert note.lilypond_format == "d'8 [ ]"


def test_Container_remove_02():
    r'''Containers remove nested containers correctly.
    Container detaches from parentage.
    Container withdraws from crossing spanners.
    Container carries covered spanners forward.
    Container returns after removal.
    '''

    staff = Staff(Container(notetools.make_repeated_notes(2)) * 2)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(staff)
    sequential = staff[0]
    p = spannertools.BeamSpanner(staff[:])

    r'''
    \new Staff {
        {
            c'8 [
            d'8
        }
        {
            e'8
            f'8 ]
        }
    }
    '''

    staff.remove(sequential)

    r'''
    \new Staff {
        {
            e'8 [
            f'8 ]
        }
    }
    '''

    assert select(staff).is_well_formed()
    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                e'8 [
                f'8 ]
            }
        }
        '''
        )

    r'''
    {
        c'8
        d'8
    }
    '''

    assert select(sequential).is_well_formed()
    assert testtools.compare(
        sequential,
        r'''
        {
            c'8
            d'8
        }
        '''
        )


def test_Container_remove_03():
    r'''Container remove works on identity and not equality.
    '''

    note = Note("c'4")
    container = Container([Note("c'4")])

    assert py.test.raises(Exception, 'container.remove(note)')
