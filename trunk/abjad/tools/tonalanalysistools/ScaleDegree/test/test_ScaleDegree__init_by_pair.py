from abjad import *
from abjad.tools import tonalanalysistools


def test_ScaleDegree__init_by_pair_01():

    degree = tonalanalysistools.ScaleDegree(('flat', 2))

    assert degree.accidental == pitchtools.Accidental('flat')
    assert degree.number == 2