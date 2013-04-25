import os
from experimental import *


def test_FileProxy_remove_01():
    '''Nonversioned file.
    '''

    score_manager_configuration = scoremanagertools.core.ScoreManagerConfiguration()
    path = os.path.join(
        score_manager_configuration.SCORE_MANAGEMENT_TOOLS_DIRECTORY_PATH, 'temporary_file.txt')
    file_proxy = scoremanagertools.proxies.FileProxy(path_name=path)
    assert not os.path.exists(path)

    try:
        file_proxy.conditionally_make_empty_asset()
        assert os.path.exists(path)
        file_proxy.remove()
        assert not os.path.exists(path)
    finally:
        if os.path.exists(path):
            os.remove(path)
        assert not os.path.exists(path)


def test_FileProxy_remove_02():
    '''Versioned file.
    '''

    score_manager_configuration = scoremanagertools.core.ScoreManagerConfiguration()
    path = os.path.join(
        score_manager_configuration.SCORE_MANAGEMENT_TOOLS_DIRECTORY_PATH, 'temporary_file.txt')
    file_proxy = scoremanagertools.proxies.FileProxy(path_name=path)
    assert not os.path.exists(path)

    try:
        file_proxy.conditionally_make_empty_asset()
        assert os.path.exists(path)
        file_proxy.svn_add()
        assert file_proxy.is_versioned
        file_proxy.remove()
        assert not os.path.exists(path)
    finally:
        if os.path.exists(path):
            os.remove(path)
        assert not os.path.exists(path)