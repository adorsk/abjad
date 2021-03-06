# -*- encoding: utf-8 -*-
from experimental import *


def test_SegmentSpecification__set_rhythm_increasing_01():
    r'''Remake of schematic example X3.
    Uses division select expressions instead of rhythm select expressions.
    Necessitates set expression decreasing=False on rhythm maker.
    '''

    score_template = templatetools.GroupedRhythmicStavesScoreTemplate(staff_count=4)
    score_specification = musicexpressiontools.ScoreSpecificationInterface(score_template)

    red_segment = score_specification.append_segment(name='red')
    red_segment.set_time_signatures([(6, 8), (3, 8)])
    measures = red_segment.select_measures('Voice 1')
    left_measure, right_measure = measures.partition_by_ratio((1, 1))
    left_measure.timespan.set_divisions([(3, 16)], contexts=['Voice 1'])
    right_measure.timespan.set_divisions([(5, 16)], contexts=['Voice 1'])
    left_measure.timespan.set_divisions([(5, 16)], contexts=['Voice 2'])
    right_measure.timespan.set_divisions([(3, 16)], contexts=['Voice 2'])

    left_half, right_half = red_segment.timespan.divide_by_ratio((1, 1))

    voice_1_left_division_set_expression = left_measure.start_offset.look_up_division_set_expression('Voice 1')
    voice_1_right_division_set_expression = right_measure.start_offset.look_up_division_set_expression('Voice 1')

    left_half.set_divisions(voice_1_left_division_set_expression, contexts=['Voice 3'])
    right_half.set_divisions(voice_1_right_division_set_expression, contexts=['Voice 3'])

    voice_2_left_division_set_expression = left_measure.start_offset.look_up_division_set_expression('Voice 2')
    voice_2_right_division_set_expression = right_measure.start_offset.look_up_division_set_expression('Voice 2')

    left_half.set_divisions(voice_2_left_division_set_expression, contexts=['Voice 4'])
    right_half.set_divisions(voice_2_right_division_set_expression, contexts=['Voice 4'])

    red_segment.set_rhythm(library.note_tokens)

    blue_segment = score_specification.append_segment(name='blue')

    red_time_signatures = red_segment.select_time_signatures('Voice 1')
    blue_segment.set_time_signatures(red_time_signatures.reflect())

    red_voice_1_divisions = red_segment.select_divisions('Voice 1')
    red_voice_2_divisions = red_segment.select_divisions('Voice 2')
    red_voice_3_divisions = red_segment.select_divisions('Voice 3')
    red_voice_4_divisions = red_segment.select_divisions('Voice 4')
    blue_segment.set_divisions(red_voice_1_divisions.reflect(), contexts=['Voice 1'])
    blue_segment.set_divisions(red_voice_2_divisions.reflect(), contexts=['Voice 2'])
    blue_segment.set_divisions(red_voice_3_divisions.reflect(), contexts=['Voice 3'])
    blue_segment.set_divisions(red_voice_4_divisions.reflect(), contexts=['Voice 4'])

    red_rhythm_set_expression = red_segment.timespan.start_offset.look_up_rhythm_set_expression('Voice 1')
    blue_segment.set_rhythm(red_rhythm_set_expression.reflect())
    score = score_specification.interpret()

    current_function_name = systemtools.TestManager.get_current_function_name()
    systemtools.TestManager.write_test_output(score, __file__, current_function_name)
    assert format(score) == systemtools.TestManager.read_test_output(__file__, current_function_name)
