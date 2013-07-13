from abjad import *


def test_TieChain_written_duration_01():

    staff = Staff("c' ~ c'16")

    assert staff[0].select_tie_chain().written_duration == Duration(5, 16)


def test_TieChain_written_duration_02():

    staff = Staff("c'")

    assert staff[0].select_tie_chain().written_duration == Duration(1, 4)