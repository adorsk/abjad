import os
from experimental import *


def test_StylesheetFileWrangler_interactively_make_asset_01():

    score_manager = scoremanagertools.scoremanager.ScoreManager()
    filesystem_path = os.path.join(
        score_manager.configuration.user_asset_library_stylesheets_directory_path, 'test-stylesheet.ly')
    assert not os.path.exists(filesystem_path)

    try:
        score_manager._run(user_input='y new 1 test-stylesheet q', is_test=True)
        assert os.path.exists(filesystem_path)
    finally:
        os.remove(filesystem_path)
        assert not os.path.exists(filesystem_path)