# -*- encoding: utf-8 -*-
import os
from experimental import *


def test_ScorePackageManager_read_only_attributes_01():
    r'''Read-only public attributes.
    '''

    package_manager = scoremanagertools.managers.ScorePackageManager(
        'scoremanagertools.scorepackages.red_example_score')

    assert isinstance(
        package_manager.segment_wrangler, 
        scoremanagertools.wranglers.SegmentPackageWrangler,
        )
    assert isinstance(
        package_manager.distribution_directory_manager, 
        scoremanagertools.managers.DirectoryManager,
        )
    assert isinstance(
        package_manager.build_directory_manager, 
        scoremanagertools.managers.DirectoryManager,
        )
    assert isinstance(
        package_manager.material_package_maker_wrangler,
        scoremanagertools.wranglers.MaterialPackageMakerWrangler,
        )
    assert isinstance(
        package_manager.material_package_wrangler,
        scoremanagertools.wranglers.MaterialPackageWrangler,
        )

    assert package_manager._get_annotated_title() == 'Red Example Score (2013)'
    assert package_manager._breadcrumb == 'Red Example Score (2013)'
    assert package_manager._get_metadata('composer') is None
    assert package_manager._get_metadata('title') == 'Red Example Score'
    assert package_manager._get_metadata('year_of_completion') == 2013
