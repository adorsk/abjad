# -*- encoding: utf-8 -*-
from experimental import *


def test_PerformerEditor_delete_instruments_01():
    r'''Quit, back, home, score & junk all work.
    '''

    score_manager = scoremanagertools.scoremanager.ScoreManager()
    score_manager._run(pending_user_input='red~example~score score~setup instrumentation hornist rm q')
    assert score_manager.session.io_transcript.signature == (11,)

    score_manager._run(pending_user_input='red~example~score score~setup instrumentation hornist rm b q')
    assert score_manager.session.io_transcript.signature == (13, (8, 11))

    score_manager._run(pending_user_input='red~example~score score~setup instrumentation hornist rm home q')
    assert score_manager.session.io_transcript.signature == (13, (0, 11))

    score_manager._run(pending_user_input='red~example~score score~setup instrumentation hornist rm score q')
    assert score_manager.session.io_transcript.signature == (13, (2, 11))

    score_manager._run(pending_user_input='red~example~score score~setup instrumentation hornist rm foo q')
    assert score_manager.session.io_transcript.signature == (13, (8, 11))


def test_PerformerEditor_delete_instruments_02():
    r'''Add two instruments. Delete one.
    '''

    editor = scoremanagertools.editors.PerformerEditor()
    editor._run(pending_user_input='add flute add acc rm flute q')
    assert editor.target == instrumenttools.Performer(instruments=[instrumenttools.Accordion()])


def test_PerformerEditor_delete_instruments_03():
    r'''Numeric range handling.
    '''

    editor = scoremanagertools.editors.PerformerEditor()
    editor._run(pending_user_input='add 1-3 rm 1,3 q')
    assert editor.target == instrumenttools.Performer(
        instruments=[instrumenttools.AltoVoice()]
        )
