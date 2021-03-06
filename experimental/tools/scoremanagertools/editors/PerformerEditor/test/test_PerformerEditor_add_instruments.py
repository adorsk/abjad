# -*- encoding: utf-8 -*-
from experimental import *


def test_PerformerEditor_add_instruments_01():
    r'''Quit, back, home, score & junk all work.
    '''

    score_manager = scoremanagertools.scoremanager.ScoreManager()
    score_manager._run(pending_user_input='red~example~score score~setup instrumentation hornist add q')
    assert score_manager.session.io_transcript.signature == (12,)

    score_manager._run(pending_user_input='red~example~score score~setup instrumentation hornist add b q')
    assert score_manager.session.io_transcript.signature == (14, (8, 12))

    score_manager._run(pending_user_input='red~example~score score~setup instrumentation hornist add home q')
    assert score_manager.session.io_transcript.signature == (14, (0, 12))

    score_manager._run(pending_user_input='red~example~score score~setup instrumentation hornist add score q')
    assert score_manager.session.io_transcript.signature == (14, (2, 12))

    score_manager._run(pending_user_input='red~example~score score~setup instrumentation hornist add foo q')
    assert score_manager.session.io_transcript.signature == (14, (10, 12))


def test_PerformerEditor_add_instruments_02():
    r'''Add two instruments.
    '''

    editor = scoremanagertools.editors.PerformerEditor()
    editor._run(pending_user_input='add 1 add 2 q')
    assert editor.target == instrumenttools.Performer(
        instruments=[
            instrumenttools.Accordion(), 
            instrumenttools.AltoVoice(),
            ])


def test_PerformerEditor_add_instruments_03():
    r'''Range handling.
    '''

    editor = scoremanagertools.editors.PerformerEditor()
    editor._run(pending_user_input='add 1-2 q')
    assert editor.target == instrumenttools.Performer(
        instruments=[
            instrumenttools.Accordion(), 
            instrumenttools.AltoVoice(),
            ])
