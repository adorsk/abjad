# -*- encoding: utf-8 -*-
from abjad import *


def test_pitchtools_Accidental_symbolic_accidental_string_01():

    assert pitchtools.Accidental('s').symbolic_accidental_string == '#'
    assert pitchtools.Accidental('ss').symbolic_accidental_string == '##'
    assert pitchtools.Accidental('f').symbolic_accidental_string == 'b'
    assert pitchtools.Accidental('ff').symbolic_accidental_string == 'bb'
    assert pitchtools.Accidental('').symbolic_accidental_string == ''


def test_pitchtools_Accidental_symbolic_accidental_string_02():

    assert pitchtools.Accidental('ff').symbolic_accidental_string == 'bb'
    assert pitchtools.Accidental('tqf').symbolic_accidental_string == 'b~'
    assert pitchtools.Accidental('f').symbolic_accidental_string == 'b'
    assert pitchtools.Accidental('qf').symbolic_accidental_string == '~'
    assert pitchtools.Accidental('').symbolic_accidental_string == ''
    assert pitchtools.Accidental('!').symbolic_accidental_string == '!'
    assert pitchtools.Accidental('qs').symbolic_accidental_string == '+'
    assert pitchtools.Accidental('s').symbolic_accidental_string == '#'
    assert pitchtools.Accidental('tqs').symbolic_accidental_string == '#+'
    assert pitchtools.Accidental('ss').symbolic_accidental_string == '##'