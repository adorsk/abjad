# -*- encoding: utf-8 -*-
from abjad import *


def test_NumberedPitch_chromatic_pitch_number_01():

    assert pitchtools.NumberedPitch(-14).chromatic_pitch_number == -14
    assert pitchtools.NumberedPitch(14).chromatic_pitch_number == 14
    assert pitchtools.NumberedPitch(-2).chromatic_pitch_number == -2
    assert pitchtools.NumberedPitch(2).chromatic_pitch_number == 2