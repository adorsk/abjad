# -*- encoding: utf-8 -*-
import pytest
from experimental import *


def test_ScoreSpecification__append_segment_01():

    score_template = templatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = musicexpressiontools.ScoreSpecificationInterface(score_template)

    red_segment = score_specification.append_segment(name='red')
    assert red_segment.segment_name == 'red'
    assert len(score_specification.specification.segment_specifications) == 1

    blue_segment = score_specification.append_segment(name='blue')
    assert blue_segment.segment_name == 'blue'
    assert len(score_specification.specification.segment_specifications) == 2


def test_ScoreSpecification__append_segment_02():
    r'''Error on duplicate segment name.
    '''

    score_template = templatetools.GroupedRhythmicStavesScoreTemplate(staff_count=1)
    score_specification = musicexpressiontools.ScoreSpecificationInterface(score_template)

    score_specification.append_segment(name='red')

    pytest.raises(Exception, "score_specification.append_segment(name='red')")
