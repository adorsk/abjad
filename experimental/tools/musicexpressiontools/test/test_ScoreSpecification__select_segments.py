# -*- encoding: utf-8 -*-
from experimental import *


def test_ScoreSpecification__select_segments_01():
    r'''Rhythm set expression anchored to segment select expression.
    '''

    score_template = templatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = musicexpressiontools.ScoreSpecificationInterface(score_template)
    red_segment = score_specification.append_segment(name='red')
    blue_segment = score_specification.append_segment(name='blue')
    green_segment = score_specification.append_segment(name='green')
    red_segment.set_time_signatures([(1, 8), (2, 8), (3, 8)])
    segments = score_specification.select_segments('Voice 1')[1:2]
    segments.timespan.set_rhythm(library.sixteenths)
    score = score_specification.interpret()
    score_specification = score_specification.specification

    current_function_name = systemtools.TestManager.get_current_function_name()
    systemtools.TestManager.write_test_output(score, __file__, current_function_name)
    assert format(score) == systemtools.TestManager.read_test_output(__file__, current_function_name)


def test_ScoreSpecification__select_segments_02():
    r'''Score-rooted set expression and segment-rooted set expression 
    made at same context.

    Score-rooted set expression occurs lexically later than segment-rooted 
    set expression.

    Score-rooted set expression overrides segment-rooted set expression.
    '''

    score_template = templatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = musicexpressiontools.ScoreSpecificationInterface(score_template)
    red_segment = score_specification.append_segment(name='red')
    blue_segment = score_specification.append_segment(name='blue')
    green_segment = score_specification.append_segment(name='green')
    red_segment.set_time_signatures([(1, 8), (2, 8), (3, 8)])
    red_segment.set_rhythm(library.sixteenths)
    segments = score_specification.select_segments('Voice 1')[1:2]
    segments.timespan.set_rhythm(library.eighths)
    score = score_specification.interpret()

    current_function_name = systemtools.TestManager.get_current_function_name()
    systemtools.TestManager.write_test_output(score, __file__, current_function_name)
    assert format(score) == systemtools.TestManager.read_test_output(__file__, current_function_name)


def test_ScoreSpecification__select_segments_03():
    r'''Two score-rooted rhythm set expressions made at same context.

    Lexically later set expression overrides lexically earlier set expression.
    '''

    score_template = templatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = musicexpressiontools.ScoreSpecificationInterface(score_template)
    red_segment = score_specification.append_segment(name='red')
    blue_segment = score_specification.append_segment(name='blue')
    green_segment = score_specification.append_segment(name='green')
    red_segment.set_time_signatures([(1, 8), (2, 8), (3, 8)])
    segments = score_specification.select_segments('Voice 1')
    segments.timespan.set_rhythm(library.sixteenths)
    segments = score_specification.select_segments('Voice 1')[1:2]
    segments.timespan.set_rhythm(library.eighths)
    score = score_specification.interpret()

    current_function_name = systemtools.TestManager.get_current_function_name()
    systemtools.TestManager.write_test_output(score, __file__, current_function_name)
    assert format(score) == systemtools.TestManager.read_test_output(__file__, current_function_name)


def test_ScoreSpecification__select_segments_04():
    r'''Two score-rooted rhythm set expressions made at different contexts.

    Lexically later set expression is also made at closer context.

    Set expression at closer context overrides set expression at more 
    distant context.
    '''

    score_template = templatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = musicexpressiontools.ScoreSpecificationInterface(score_template)
    red_segment = score_specification.append_segment(name='red')
    blue_segment = score_specification.append_segment(name='blue')
    green_segment = score_specification.append_segment(name='green')
    red_segment.set_time_signatures([(1, 8), (2, 8), (3, 8)])
    score_specification.set_rhythm(library.sixteenths)
    segments = score_specification.select_segments('Voice 1')[1:2]
    segments.timespan.set_rhythm(library.eighths, contexts=['Voice 1'])
    score = score_specification.interpret()

    current_function_name = systemtools.TestManager.get_current_function_name()
    systemtools.TestManager.write_test_output(score, __file__, current_function_name)
    assert format(score) == systemtools.TestManager.read_test_output(__file__, current_function_name)


def test_ScoreSpecification__select_segments_05():
    r'''Two score-rooted rhythm set expressions made at different contexts.

    Lexically later set expression is also made at more distant context.

    Set expression at closer context overrides set expression at more 
    distant context.
    '''

    score_template = templatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = musicexpressiontools.ScoreSpecificationInterface(score_template)
    red_segment = score_specification.append_segment(name='red')
    blue_segment = score_specification.append_segment(name='blue')
    green_segment = score_specification.append_segment(name='green')
    red_segment.set_time_signatures([(1, 8), (2, 8), (3, 8)])
    segments = score_specification.select_segments('Voice 1')[1:2]
    segments.timespan.set_rhythm(library.eighths, contexts=['Voice 1'])
    score_specification.set_rhythm(library.sixteenths)
    score = score_specification.interpret()

    current_function_name = systemtools.TestManager.get_current_function_name()
    systemtools.TestManager.write_test_output(score, __file__, current_function_name)
    assert format(score) == systemtools.TestManager.read_test_output(__file__, current_function_name)


def test_ScoreSpecification__select_segments_06():
    r'''Single-integer positive getitem index.
    '''

    score_template = templatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = musicexpressiontools.ScoreSpecificationInterface(score_template)
    red_segment = score_specification.append_segment(name='red')
    blue_segment = score_specification.append_segment(name='blue')
    green_segment = score_specification.append_segment(name='green')
    red_segment.set_time_signatures([(1, 8), (2, 8), (3, 8)])
    red_segment.set_rhythm(library.sixteenths)
    segment = score_specification.select_segments('Voice 1')[1]
    segment.timespan.select_leaves('Voice 1').set_spanner(spannertools.Slur())
    score = score_specification.interpret()

    current_function_name = systemtools.TestManager.get_current_function_name()
    systemtools.TestManager.write_test_output(score, __file__, current_function_name)
    assert format(score) == systemtools.TestManager.read_test_output(__file__, current_function_name)


def test_ScoreSpecification__select_segments_07():
    r'''Single-integer negative getitem index.
    '''

    score_template = templatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = musicexpressiontools.ScoreSpecificationInterface(score_template)
    red_segment = score_specification.append_segment(name='red')
    blue_segment = score_specification.append_segment(name='blue')
    green_segment = score_specification.append_segment(name='green')
    red_segment.set_time_signatures([(1, 8), (2, 8), (3, 8)])
    red_segment.set_rhythm(library.sixteenths)
    segment = score_specification.select_segments('Voice 1')[-2]
    segment.timespan.select_leaves('Voice 1').set_spanner(spannertools.Slur())
    score = score_specification.interpret()

    current_function_name = systemtools.TestManager.get_current_function_name()
    systemtools.TestManager.write_test_output(score, __file__, current_function_name)
    assert format(score) == systemtools.TestManager.read_test_output(__file__, current_function_name)
