# -*- encoding: utf-8 -*-
from abjad import *


def test_pitchtools_pitch_class_name_to_pitch_class_number_01():

    assert pitchtools.pitch_class_name_to_pitch_class_number('cff') == 10
    assert pitchtools.pitch_class_name_to_pitch_class_number('ctqf') == 10.5
    assert pitchtools.pitch_class_name_to_pitch_class_number('cf') == 11
    assert pitchtools.pitch_class_name_to_pitch_class_number('cqf') == 11.5
    assert pitchtools.pitch_class_name_to_pitch_class_number('c') == 0
    assert pitchtools.pitch_class_name_to_pitch_class_number('cqs') == 0.5
    assert pitchtools.pitch_class_name_to_pitch_class_number('cs') == 1
    assert pitchtools.pitch_class_name_to_pitch_class_number('ctqs') == 1.5
    assert pitchtools.pitch_class_name_to_pitch_class_number('css') == 2