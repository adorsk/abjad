# -*- encoding: utf-8 -*-
from abjad import *


def test_rhythmmakertools_TaleaRhythmMaker_burnish_output_01():

    burnish_specifier = rhythmmakertools.BurnishSpecifier(
        lefts=(0,), 
        middles=(-1,), 
        rights=(0,), 
        left_lengths=(1,), 
        right_lengths=(1,),
        )

    maker = rhythmmakertools.TaleaRhythmMaker(
        talea=(1,), 
        talea_denominator=16, 
        burnish_specifier=burnish_specifier,
        prolation_addenda=(2,),
        burnish_output=True,
        )

    divisions = [(3, 16), (3, 8)]
    music = maker(divisions)

    music = sequencetools.flatten_sequence(music)
    measures = scoretools.make_spacer_skip_measures(divisions)
    staff = Staff(measures)
    mutate(staff).replace_measure_contents(music)

    assert systemtools.TestManager.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 3/16
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 3/5 {
                    c'16
                    r16
                    r16
                    r16
                    r16
                }
            }
            {
                \time 3/8
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 3/4 {
                    r16
                    r16
                    r16
                    r16
                    r16
                    r16
                    r16
                    c'16
                }
            }
        }
        '''
        )


def test_rhythmmakertools_TaleaRhythmMaker_burnish_output_02():

    burnish_specifier = rhythmmakertools.BurnishSpecifier(
        lefts=(-1,), 
        middles=(0,), 
        rights=(-1,), 
        left_lengths=(1,), 
        right_lengths=(1,),
        )

    maker = rhythmmakertools.TaleaRhythmMaker(
        talea=(1,), 
        talea_denominator=4, 
        burnish_specifier=burnish_specifier,
        prolation_addenda=(2,),
        burnish_output=True,
        )

    divisions = [(3, 16), (3, 8)]
    music = maker(divisions)

    music = sequencetools.flatten_sequence(music)
    measures = scoretools.make_spacer_skip_measures(divisions)
    staff = Staff(measures)
    mutate(staff).replace_measure_contents(music)

    assert systemtools.TestManager.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 3/16
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 3/5 {
                    r4
                    c'16
                }
            }
            {
                \time 3/8
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 3/4 {
                    c'8.
                    c'4
                    r16
                }
            }
        }
        '''
        )


def test_rhythmmakertools_TaleaRhythmMaker_burnish_output_03():

    burnish_specifier = rhythmmakertools.BurnishSpecifier(
        lefts=(-1,), 
        middles=(0,), 
        rights=(-1,), 
        left_lengths=(1,), 
        right_lengths=(1,), 
        )

    maker = rhythmmakertools.TaleaRhythmMaker(
        talea=(1, 2, 3), 
        talea_denominator=16, 
        burnish_specifier=burnish_specifier,
        prolation_addenda=(0, 2),
        secondary_divisions=(9,),
        burnish_output=True,
        )

    divisions = [(3, 8), (4, 8)]
    music = maker(divisions)

    music = sequencetools.flatten_sequence(music)
    measures = scoretools.make_spacer_skip_measures(divisions)
    staff = Staff(measures)
    mutate(staff).replace_measure_contents(music)

    assert systemtools.TestManager.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 3/8
                {
                    r16
                    c'8
                    c'8.
                }
            }
            {
                \time 4/8
                \tweak #'text #tuplet-number::calc-fraction-text
                \times 3/5 {
                    c'16
                    c'8
                    c'8
                }
                {
                    c'16
                    c'16
                    c'8
                    r16
                }
            }
        }
        '''
        )


def test_rhythmmakertools_TaleaRhythmMaker_burnish_output_04():

    burnish_specifier = rhythmmakertools.BurnishSpecifier(
        lefts=(-1,), 
        middles=(0,), 
        rights=(-1,),
        left_lengths=(1,), 
        right_lengths=(2,),
        )

    maker = rhythmmakertools.TaleaRhythmMaker(
        talea=(1,), 
        talea_denominator=8, 
        burnish_specifier=burnish_specifier,
        prolation_addenda=(),
        burnish_output=True,
        )

    divisions = [(8, 8)]
    music = maker(divisions)

    music = sequencetools.flatten_sequence(music)
    measures = scoretools.make_spacer_skip_measures(divisions)
    staff = Staff(measures)
    mutate(staff).replace_measure_contents(music)

    assert systemtools.TestManager.compare(
        staff,
        r'''
        \new Staff {
            {
                \time 8/8
                r8
                c'8
                c'8
                c'8
                c'8
                c'8
                r8
                r8
            }
        }
        '''
        )
