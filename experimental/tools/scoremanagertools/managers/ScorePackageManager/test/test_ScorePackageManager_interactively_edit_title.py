# -*- encoding: utf-8 -*-
import pytest
from experimental import *
pytest.skip('unskip me after making decision about cache.')


def test_ScorePackageManager_interactively_edit_title_01():

    try:
        score_manager = scoremanagertools.scoremanager.ScoreManager()
        score_manager._run(pending_user_input='green~example~score score~setup title Foo q')
        assert score_manager.session.io_transcript.signature == (9,)
        assert score_manager.session.io_transcript[-5][1][0] == 'Green Example Score (2013) - setup'
        assert score_manager.session.io_transcript[-2][1][0] == 'Foo (2013) - setup'
    finally:
        score_manager._run(pending_user_input='foo score~setup title Green~Example~Score q')
        assert score_manager.session.io_transcript.signature == (9,)
        assert score_manager.session.io_transcript[-5][1][0] == 'Foo (2013) - setup'
        assert score_manager.session.io_transcript[-2][1][0] == 'Green Example Score (2013) - setup'
