# -*- encoding: utf-8 -*-
from abjad import *
import py.test


def test_markuptools_MarkupCommand___setattr___01():

    a = markuptools.MarkupCommand('draw-circle', 1, 0.1, False)
    assert py.test.raises(AttributeError, "a.foo = 'bar'")