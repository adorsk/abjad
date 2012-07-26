from experimental import quantizationtools
import copy


def test_QGridLeaf___copy___01():

    leaf = quantizationtools.QGridLeaf(1)

    copied = copy.copy(leaf)

    assert leaf == copied
    assert leaf is not copied


def test_QGridLeaf___copy___02():

    leaf = quantizationtools.QGridLeaf(2, [quantizationtools.SilentQEvent(1000)])

    copied = copy.copy(leaf)

    assert leaf == copied
    assert leaf is not copied
