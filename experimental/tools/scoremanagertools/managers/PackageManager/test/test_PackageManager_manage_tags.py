# -*- encoding: utf-8 -*-
from experimental import *


def test_PackageManager_manage_tags_01():
    r'''Quit, back, home, score & junk all work.
    '''

    score_manager = scoremanagertools.scoremanager.ScoreManager()
    score_manager._run(pending_user_input='red~example~score tags q')
    assert score_manager.session.io_transcript.signature == (6,)

    score_manager._run(pending_user_input='red~example~score tags b q')
    assert score_manager.session.io_transcript.signature == (8, (2, 6))

    score_manager._run(pending_user_input='red~example~score tags home q')
    assert score_manager.session.io_transcript.signature == (8, (0, 6))

    score_manager._run(pending_user_input='red~example~score tags score q')
    assert score_manager.session.io_transcript.signature == (8, (2, 6))

    score_manager._run(pending_user_input='red~example~score tags foo q')
    assert score_manager.session.io_transcript.signature == (8, (4, 6))
