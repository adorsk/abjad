from abjad.tools.timeintervaltools import *
from abjad.tools.timeintervaltools._make_test_intervals import _make_test_intervals
from fractions import Fraction


def test_timeintervaltools_calculate_sustain_centroid_of_intervals_01():
    tree = TimeIntervalTree(_make_test_intervals())
    result = calculate_sustain_centroid_of_intervals(tree)
    assert result == Fraction(1619, 90)


def test_timeintervaltools_calculate_sustain_centroid_of_intervals_02():
    tree = TimeIntervalTree([])
    result = calculate_sustain_centroid_of_intervals(tree)
    assert result is None
