# -*- encoding: utf-8 -*-
from experimental.tools.musicexpressiontools.Division import Division


def test_Division___add___01():

    assert Division((4, 8)) + Division((2, 8)) == Division((6, 8))
    assert Division((4, 8)) + Division((1, 16)) == Division((9, 16))
