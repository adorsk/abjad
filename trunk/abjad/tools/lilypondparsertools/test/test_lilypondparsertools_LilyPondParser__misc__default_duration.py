# -*- encoding: utf-8 -*-
import py.test
from abjad import *
from abjad.tools.lilypondparsertools import LilyPondParser


def test_lilypondparsertools_LilyPondParser__misc__default_duration_01():
    target = Container(notetools.make_notes([0],
        [(1, 4), (1, 2), (1, 2), (1, 8), (1, 8), (3, 16), (3, 16)]))
    target[-2].lilypond_duration_multiplier = Fraction(5, 17)
    target[-1].lilypond_duration_multiplier = Fraction(5, 17)

    r'''
    {
        c'4
        c'2
        c'2
        c'8
        c'8
        c'8. * 5/17
        c'8. * 5/17
    }
    '''

    input = r'''{ c' c'2 c' c'8 c' c'8. * 5/17 c' }'''

    parser = LilyPondParser()
    result = parser(input)
    assert target.lilypond_format == result.lilypond_format and target is not result