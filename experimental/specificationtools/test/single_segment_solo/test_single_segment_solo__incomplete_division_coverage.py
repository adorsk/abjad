from abjad import *
from experimental import *


def test_single_segment_solo__incomplete_division_coverage_01():
    '''Divisions cover only middle measure.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    red_segment = score_specification.append_segment(name='red')
    red_segment.set_time_signatures([(4, 8), (3, 8), (2, 8)])
    selector = red_segment.select_background_measures(1, 2)
    red_segment.set_divisions([(2, 16)], selector=selector)
    red_segment.set_rhythm(library.sixteenths)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo__incomplete_division_coverage_02():
    '''Divisions cover only first and last measures.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    red_segment = score_specification.append_segment(name='red')
    red_segment.set_time_signatures([(4, 8), (3, 8), (2, 8)])
    selector = red_segment.select_background_measures(0, 1)
    red_segment.set_divisions([(3, 16)], selector=selector)
    selector = red_segment.select_background_measures(-1)
    red_segment.set_divisions([(2, 16)], selector=selector)
    red_segment.set_rhythm(library.sixteenths)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo__incomplete_division_coverage_03():
    '''Contexts and selector work together.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    red_segment = score_specification.append_segment(name='red')
    red_segment.set_time_signatures([(4, 8), (3, 8), (2, 8)])
    selector = red_segment.select_background_measures(1, 2)
    red_segment.set_divisions([(2, 16)], selector=selector)
    red_segment.set_divisions([(2, 16)], contexts=['Voice 1'], selector=selector)
    red_segment.set_rhythm(library.sixteenths)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo__incomplete_division_coverage_04():
    '''Contexts and selector work together.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    red_segment = score_specification.append_segment(name='red')
    red_segment.set_time_signatures([(4, 8), (3, 8), (2, 8)])
    selector = red_segment.select_background_measures(0, 1)
    red_segment.set_divisions([(3, 16)], selector=selector)
    selector = red_segment.select_background_measures(-1)
    red_segment.set_divisions([(2, 16)], contexts=['Voice 1'], selector=selector)
    red_segment.set_rhythm(library.sixteenths)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo__incomplete_division_coverage_05():
    '''One selector partially covers the other.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    red_segment = score_specification.append_segment(name='red')
    red_segment.set_time_signatures([(4, 8), (3, 8), (2, 8)])
    selector = red_segment.select_background_measures(start=-2)
    red_segment.set_divisions([(2, 16)], selector=selector)
    selector = red_segment.select_background_measures(start=-1)
    red_segment.set_divisions([(3, 16)], selector=selector)
    red_segment.set_rhythm(library.sixteenths)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo__incomplete_division_coverage_06():
    '''One selector partially covers the other. Works with contexts.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    red_segment = score_specification.append_segment(name='red')
    red_segment.set_time_signatures([(4, 8), (3, 8), (2, 8)])
    selector = red_segment.select_background_measures(start=-2)
    red_segment.set_divisions([(2, 16)], selector=selector)
    selector = red_segment.select_background_measures(start=-1)
    red_segment.set_divisions([(3, 16)], contexts=['Voice 1'], selector=selector)
    red_segment.set_rhythm(library.sixteenths)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo__incomplete_division_coverage_07():
    '''One selector more important than the other.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    red_segment = score_specification.append_segment(name='red')
    red_segment.set_time_signatures([(4, 8), (3, 8), (2, 8)])
    selector = red_segment.select_background_measures(start=-2)
    red_segment.set_divisions([(2, 16)], contexts=['Voice 1'], selector=selector)
    selector = red_segment.select_background_measures(start=-1)
    red_segment.set_divisions([(3, 16)], selector=selector)
    red_segment.set_rhythm(library.sixteenths)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)


def test_single_segment_solo__incomplete_division_coverage_08():
    '''Division selector cuts fractional chunks out of time signatures.
    '''

    score_template = scoretemplatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = specificationtools.ScoreSpecification(score_template)
    red_segment = score_specification.append_segment(name='red')
    red_segment.set_time_signatures(3 * [(4, 8)])
    segment = red_segment.select()
    selector = segment.adjust_offsets(start=(10, 16), stop=(13, 16))
    red_segment.set_divisions([(2, 32)], selector=selector)
    red_segment.set_rhythm(library.thirty_seconds)
    score = score_specification.interpret()

    current_function_name = introspectiontools.get_current_function_name()
    helpertools.write_test_output(score, __file__, current_function_name)
    assert score.lilypond_format == helpertools.read_test_output(__file__, current_function_name)
