# -*- encoding: utf-8 -*-
from abjad import *


def test_instrumenttools_AltoFlute_sounding_pitch_of_written_middle_c_01():

    alto_flute = instrumenttools.AltoFlute()

    assert alto_flute.sounding_pitch_of_written_middle_c == 'g'