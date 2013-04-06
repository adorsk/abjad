from abjad import *
import scf


def test_TempoMarkEditor_run_01():

    editor = scf.editors.TempoMarkEditor()
    editor.run(user_input='q')
    assert editor.target is None


def test_TempoMarkEditor_run_02():

    editor = scf.editors.TempoMarkEditor()
    editor.run(user_input='duration (1, 8) units 98 q')
    assert editor.target == contexttools.TempoMark(Duration(1, 8), 98)


def test_TempoMarkEditor_run_03():

    editor = scf.editors.TempoMarkEditor()
    editor.run(user_input='duration Duration(1, 8) units 98 q')
    assert editor.target == contexttools.TempoMark(Duration(1, 8), 98)