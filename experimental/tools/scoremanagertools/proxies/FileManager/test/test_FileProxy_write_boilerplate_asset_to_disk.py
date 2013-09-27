# -*- encoding: utf-8 -*-
import os
from experimental import *


def test_FileManager_write_boilerplate_asset_to_disk_01():

    score_manager_configuration = scoremanagertools.scoremanager.ScoreManagerConfiguration()
    filesystem_path = os.path.join(
        score_manager_configuration.score_manager_tools_directory_path, 'temporary_file.txt')
    file_proxy = scoremanagertools.proxies.FileManager(filesystem_path=filesystem_path)
    assert not os.path.exists(filesystem_path)

    try:
        boilerplate_filebuilt_in_asset_name = 'canned_testnumbers_material_definition.py'
        file_proxy.write_boilerplate(boilerplate_filebuilt_in_asset_name)
        source = open(os.path.join(
            file_proxy.boilerplate_directory_path, boilerplate_filebuilt_in_asset_name), 'r')
        target = open(file_proxy.filesystem_path)
        assert source.readlines() == target.readlines()
        file_proxy.remove()
    finally:
        if os.path.exists(filesystem_path):
            os.remove(filesystem_path)
        assert not os.path.exists(filesystem_path)