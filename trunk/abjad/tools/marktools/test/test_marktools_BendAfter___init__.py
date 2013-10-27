# -*- encoding: utf-8 -*-
from abjad import *


def test_marktools_BendAfter___init___01():
    r'''Initialize bend from bend amount.
    '''

    bend = marktools.BendAfter(16)
    assert isinstance(bend, marktools.BendAfter)


def test_marktools_BendAfter___init___02():
    r'''Initialize bend from other bend.
    '''

    bend_1 = marktools.BendAfter(16)
    bend_2 = marktools.BendAfter(bend_1)

    assert isinstance(bend_1, marktools.BendAfter)
    assert isinstance(bend_2, marktools.BendAfter)
    assert bend_1 == bend_2
    assert bend_1 is not bend_2