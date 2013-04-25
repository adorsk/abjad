import os
from experimental import *


def test_ScoreManagerObject_public_methods_01():

    score_manager_object = scoremanagertools.core.ScoreManagerObject()

    path = os.path.join(
        score_manager_object.configuration.SCORE_MANAGEMENT_TOOLS_DIRECTORY_PATH, 
        'scoremanager', 'ScoreManager', 'ScoreManager.py')
    assert score_manager_object.module_importable_name_to_path_name(
        'scoremanagertools.scoremanager.ScoreManager.ScoreManager') == path

    path = score_manager_object.configuration.SCORE_MANAGEMENT_TOOLS_DIRECTORY_PATH
    assert score_manager_object.package_importable_name_to_path_name('scoremanagertools') == path