# -*- encoding: utf-8 -*-
import py
from abjad import *


def test_mutationtools_ScoreMutationAgent_fuse_01():
    r'''Works with list of leaves.
    '''

    notes = scoretools.make_repeated_notes(8, Duration(1, 4))
    fused = mutate(notes).fuse()

    assert len(fused) == 1
    assert fused[0].written_duration == Duration(2)


def test_mutationtools_ScoreMutationAgent_fuse_02():
    r'''Works with Leaf component.
    '''

    fused = mutate(Note("c'4")).fuse()
    assert len(fused) == 1
    assert fused[0].written_duration == Duration(1, 4)


def test_mutationtools_ScoreMutationAgent_fuse_03():
    r'''Works with containers.
    '''

    voice = Voice(Note("c'4") * 8)
    fused = mutate(voice[:]).fuse()
    assert len(fused) == 1
    assert fused[0].written_duration == 2
    assert voice[0] is fused[0]


def test_mutationtools_ScoreMutationAgent_fuse_04():
    r'''Fusion results in tied notes.
    '''

    voice = Voice([Note(0, (2, 16)), Note(9, (3, 16))])
    fused = mutate(voice[:]).fuse()
    assert len(fused) == 2
    assert fused[0].written_duration == Duration(1, 4)
    assert fused[1].written_duration == Duration(1, 16)
    tie_1 = inspect(fused[0]).get_spanner(spannertools.TieSpanner)
    tie_2 = inspect(fused[1]).get_spanner(spannertools.TieSpanner)
    assert tie_1 is tie_2
    assert voice[0] is fused[0]
    assert voice[1] is fused[1]
    assert voice[0].written_pitch.numbered_pitch == \
        voice[1].written_pitch.numbered_pitch


def test_mutationtools_ScoreMutationAgent_fuse_05():
    r'''Fuse leaves with differing LilyPond multipliers.
    '''

    staff = Staff([scoretools.Skip((1, 1)), scoretools.Skip((1, 1))])
    staff[0].lilypond_duration_multiplier = Duration(1, 16)
    staff[1].lilypond_duration_multiplier = Duration(5, 16)

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            s1 * 1/16
            s1 * 5/16
        }
        '''
        )

    assert inspect(staff).get_duration() == Duration(3, 8)

    mutate(staff[:]).fuse()

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            s1 * 3/8
        }
        '''
        )

    assert inspect(staff).get_duration() == Duration(3, 8)
    assert inspect(staff).is_well_formed()


def test_mutationtools_ScoreMutationAgent_fuse_06():
    r'''Fuse two unincorporated fixed-duration tuplets with same multiplier.
    '''

    tuplet_1 = scoretools.FixedDurationTuplet(
        Duration(2, 8), "c'8 d'8 e'8")
    beam = spannertools.BeamSpanner()
    attach(beam, tuplet_1[:])
    tuplet_2 = scoretools.FixedDurationTuplet(
        Duration(2, 16), "c'16 d'16 e'16")
    slur = spannertools.SlurSpanner()
    attach(slur, tuplet_2[:])

    assert testtools.compare(
        tuplet_1,
        r'''
        \times 2/3 {
            c'8 [
            d'8
            e'8 ]
        }
        '''
        )

    assert testtools.compare(
        tuplet_2,
        r'''
        \times 2/3 {
            c'16 (
            d'16
            e'16 )
        }
        '''
        )

    tuplets = select([tuplet_1, tuplet_2], contiguous=True)
    new = mutate(tuplets).fuse()

    assert testtools.compare(
        new,
        r'''
        \times 2/3 {
            c'8 [
            d'8
            e'8 ]
            c'16 (
            d'16
            e'16 )
        }
        '''
        )

    assert len(tuplet_1) == 0
    assert len(tuplet_2) == 0
    assert new is not tuplet_1 and new is not tuplet_2
    assert inspect(new).is_well_formed()


def test_mutationtools_ScoreMutationAgent_fuse_07():
    r'''Fuse fixed-duration tuplets with same multiplier in score.
    '''

    tuplet_1 = scoretools.FixedDurationTuplet(
        Duration(2, 8), "c'8 d'8 e'8")
    beam = spannertools.BeamSpanner()
    attach(beam, tuplet_1[:])
    tuplet_2 = scoretools.FixedDurationTuplet(
        Duration(2, 16), "c'16 d'16 e'16")
    slur = spannertools.SlurSpanner()
    attach(slur, tuplet_2[:])
    voice = Voice([tuplet_1, tuplet_2])

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            \times 2/3 {
                c'8 [
                d'8
                e'8 ]
            }
            \times 2/3 {
                c'16 (
                d'16
                e'16 )
            }
        }
        '''
        )

    tuplets = voice[:]
    mutate(tuplets).fuse()

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            \times 2/3 {
                c'8 [
                d'8
                e'8 ]
                c'16 (
                d'16
                e'16 )
            }
        }
        '''
        )

    assert inspect(voice).is_well_formed()


def test_mutationtools_ScoreMutationAgent_fuse_08():
    r'''Fuse fixed-multiplier tuplets with same multiplier in score.
    '''

    tuplet_1 = Tuplet(Multiplier(2, 3), "c'8 d'8 e'8")
    beam = spannertools.BeamSpanner()
    attach(beam, tuplet_1[:])
    tuplet_2 = Tuplet(Multiplier(2, 3), "c'8 d'8 e'8 f'8 g'8")
    slur = spannertools.SlurSpanner()
    attach(slur, tuplet_2[:])
    voice = Voice([tuplet_1, tuplet_2])

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            \times 2/3 {
                c'8 [
                d'8
                e'8 ]
            }
            \times 2/3 {
                c'8 (
                d'8
                e'8
                f'8
                g'8 )
            }
        }
        '''
        )

    tuplets = voice[:]
    mutate(tuplets).fuse()

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            \times 2/3 {
                c'8 [
                d'8
                e'8 ]
                c'8 (
                d'8
                e'8
                f'8
                g'8 )
            }
        }
        '''
        )

    assert inspect(voice).is_well_formed()


def test_mutationtools_ScoreMutationAgent_fuse_09():
    r'''Tuplets must carry same multiplier.
    '''

    tuplet_1 = scoretools.FixedDurationTuplet(Duration(2, 8), "c'8 d'8 e'8")
    tuplet_2 = scoretools.FixedDurationTuplet(
        Duration(2, 8), "c'8 d'8 e'8 f'8 g'8")
    tuplets = select([tuplet_1, tuplet_2], contiguous=True)

    assert py.test.raises(Exception, 'mutate(tuplets).fuse()')


def test_mutationtools_ScoreMutationAgent_fuse_10():
    r'''Tuplets must be same type.
    '''

    tuplet_1 = scoretools.FixedDurationTuplet(Duration(2, 8), "c'8 d'8 e'8")
    tuplet_2 = Tuplet(Multiplier(2, 3), "c'8 d'8 e'8")
    tuplets = select([tuplet_1, tuplet_2], contiguous=True)

    assert py.test.raises(Exception, 'mutate(tuplets).fuse()')


def test_mutationtools_ScoreMutationAgent_fuse_11():
    r'''Dominant spanners on contents are preserved.
    '''

    voice = Voice([
        scoretools.FixedDurationTuplet(Duration(1, 12), [Note(0, (1, 8))]),
        scoretools.FixedDurationTuplet(Duration(1, 6), [Note("c'4")]),
        Note("c'4")])
    slur = spannertools.SlurSpanner()
    attach(slur, voice.select_leaves())

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            \times 2/3 {
                c'8 (
            }
            \times 2/3 {
                c'4
            }
            c'4 )
        }
        '''
        )

    tuplets = voice[:2]
    mutate(tuplets).fuse()

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            \times 2/3 {
                c'8 (
                c'4
            }
            c'4 )
        }
        '''
        )

    assert inspect(voice).is_well_formed()


def test_mutationtools_ScoreMutationAgent_fuse_12():
    r'''Fuse unicorporated measures carrying
    time signatures with power-of-two denominators.
    '''
    
    measure_1 = Measure((1, 8), "c'16 d'16")
    beam = spannertools.BeamSpanner()
    attach(beam, measure_1[:])
    measure_2 = Measure((2, 16), "c'16 d'16")
    slur = spannertools.SlurSpanner()
    attach(slur, measure_2[:])
    staff = Staff([measure_1, measure_2])

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 1/8
                c'16 [
                d'16 ]
            }
            {
                \time 2/16
                c'16 (
                d'16 )
            }
        }
        '''
        )

    new = mutate(staff[:]).fuse()

    assert new is not measure_1 and new is not measure_2
    assert len(measure_1) == 0
    assert len(measure_2) == 0

    assert testtools.compare(
        new,
        r'''
        {
            \time 2/8
            c'16 [
            d'16 ]
            c'16 (
            d'16 )
        }
        '''
        )

    assert inspect(new).is_well_formed()


def test_mutationtools_ScoreMutationAgent_fuse_13():
    r'''Fuse measures carrying time signatures with differing 
    power-of-two denominators. Helpers selects minimum of two denominators.
    Beams are OK because they attach to leaves rather than containers.
    '''

    voice = Voice("abj: | 1/8 c'16 d'16 || 2/16 e'16 f'16 |")
    beam = spannertools.BeamSpanner()
    attach(beam, voice.select_leaves())

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            {
                \time 1/8
                c'16 [
                d'16
            }
            {
                \time 2/16
                e'16
                f'16 ]
            }
        }
        '''
        )

    mutate(voice[:]).fuse()

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            {
                \time 2/8
                c'16 [
                d'16
                e'16
                f'16 ]
            }
        }
        '''
        )

    assert inspect(voice).is_well_formed()


def test_mutationtools_ScoreMutationAgent_fuse_14():
    r'''Fuse measures with differing power-of-two denominators.
    Helpers selects minimum of two denominators.
    Beam attaches to container rather than leaves.
    '''

    voice = Voice("abj: | 1/8 c'16 d'16 || 2/16 e'16 f'16 |")
    beam = spannertools.BeamSpanner()
    attach(beam, voice[0])

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            {
                \time 1/8
                c'16 [
                d'16 ]
            }
            {
                \time 2/16
                e'16
                f'16
            }
        }
        '''
        )

    mutate(voice[:]).fuse()

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            {
                \time 2/8
                c'16
                d'16
                e'16
                f'16
            }
        }
        '''
        )

    assert inspect(voice).is_well_formed()


def test_mutationtools_ScoreMutationAgent_fuse_15():
    r'''Fuse measures with power-of-two-denominators together with measures
    without power-of-two denominators.
    Helpers selects least common multiple of denominators.
    Beams are OK because they attach to leaves rather than containers.
    '''

    measure_1 = Measure((1, 8), "c'8")
    measure_2 = Measure((1, 12), "d'8")
    voice = Voice([measure_1, measure_2])
    beam = spannertools.BeamSpanner()
    attach(beam, voice.select_leaves())

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            {
                \time 1/8
                c'8 [
            }
            {
                \time 1/12
                \scaleDurations #'(2 . 3) {
                    d'8 ]
                }
            }
        }
        '''
        )

    mutate(voice[:]).fuse()

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            {
                \time 5/24
                \scaleDurations #'(2 . 3) {
                    c'8. [
                    d'8 ]
                }
            }
        }
        '''
        )

    assert inspect(voice).is_well_formed()


def test_mutationtools_ScoreMutationAgent_fuse_16():
    r'''Fusing empty selection returns none.
    '''

    staff = Staff()
    result = mutate(staff[:]).fuse()
    assert result == selectiontools.ContiguousSelection()


def test_mutationtools_ScoreMutationAgent_fuse_17():
    r'''Fusing selection of only one measure returns measure unaltered.
    '''

    measure = Measure((3, 8), "c'8 d'8 e'8")
    staff = Staff([measure])
    new = mutate(staff[:]).fuse()

    assert new is measure


def test_mutationtools_ScoreMutationAgent_fuse_18():
    r'''Fuse three measures.
    '''

    voice = Voice("abj: | 1/8 c'16 d'16 || 1/8 e'16 f'16 || 1/8 g'16 a'16 |")
    beam = spannertools.BeamSpanner()
    attach(beam, voice.select_leaves())

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            {
                \time 1/8
                c'16 [
                d'16
            }
            {
                e'16
                f'16
            }
            {
                g'16
                a'16 ]
            }
        }
        '''
        )

    mutate(voice[:]).fuse()

    assert testtools.compare(
        voice,
        r'''
        \new Voice {
            {
                \time 3/8
                c'16 [
                d'16
                e'16
                f'16
                g'16
                a'16 ]
            }
        }
        '''
        )

    assert inspect(voice).is_well_formed()


def test_mutationtools_ScoreMutationAgent_fuse_19():
    r'''Fusing measures with power-of-two denominators
    to measures without power-of-two denominators.
    With change in number of note heads because of non-power-of-two multiplier.
    '''

    staff = Staff([
        Measure((9, 80), []),
        Measure((2, 16), [])])
    scoretools.fill_measures_in_expr_with_time_signature_denominator_notes(
        staff)

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 9/80
                \scaleDurations #'(4 . 5) {
                    c'64
                    c'64
                    c'64
                    c'64
                    c'64
                    c'64
                    c'64
                    c'64
                    c'64
                }
            }
            {
                \time 2/16
                c'16
                c'16
            }
        }
        '''
        )

    new = mutate(staff[:]).fuse()

    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 19/80
                \scaleDurations #'(4 . 5) {
                    c'64
                    c'64
                    c'64
                    c'64
                    c'64
                    c'64
                    c'64
                    c'64
                    c'64
                    c'16 ~
                    c'64
                    c'16 ~
                    c'64
                }
            }
        }
        '''
        )

    assert inspect(staff).is_well_formed()