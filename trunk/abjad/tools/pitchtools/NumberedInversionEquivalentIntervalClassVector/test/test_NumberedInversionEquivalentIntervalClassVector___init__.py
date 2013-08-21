# -*- encoding: utf-8 -*-
from abjad import *


def test_NumberedInversionEquivalentIntervalClassVector___init___01():
    r'''Init inversion-equivalent chromatic interval-class vector from list of numbers.
    '''

    iecicv = pitchtools.NumberedInversionEquivalentIntervalClassVector([1, 1, 6, 2, 2, 2])

    assert sorted(iecicv.items()) == [
        (0, 0), (0.5, 0), (1, 2), (1.5, 0), (2, 3), (2.5, 0), (3, 0), (3.5, 0),
        (4, 0), (4.5, 0), (5, 0), (5.5, 0), (6, 1)]


def test_NumberedInversionEquivalentIntervalClassVector___init___02():
    r'''Init inversion-equivalent chromatic interval-class vector from interval-class counts.
    '''

    iecicv = pitchtools.NumberedInversionEquivalentIntervalClassVector(
        counts = [2, 3, 0, 0, 0, 1])

    assert sorted(iecicv.items()) == [
        (0, 0), (0.5, 0), (1, 2), (1.5, 0), (2, 3), (2.5, 0), (3, 0), (3.5, 0),
        (4, 0), (4.5, 0), (5, 0), (5.5, 0), (6, 1)]