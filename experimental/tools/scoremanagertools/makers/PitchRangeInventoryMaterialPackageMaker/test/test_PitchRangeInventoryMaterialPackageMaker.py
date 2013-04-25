from abjad.tools import pitchtools
from experimental import *


def test_PitchRangeInventoryMaterialPackageMaker_01():
    '''Stub material package.
    '''

    score_manager = scoremanagertools.scoremanager.ScoreManager()
    assert not score_manager.package_exists('materials.testpir')
    try:
        score_manager.run(user_input=
            'materials maker pitch testpir default '
            'q'
            )
        mpp = scoremanagertools.makers.PitchRangeInventoryMaterialPackageMaker('materials.testpir')
        assert mpp.directory_contents == ['__init__.py', 'tags.py']
        assert mpp.output_material is None
    finally:
        score_manager.run(user_input='m testpir del remove default q')
        assert not score_manager.package_exists('materials.testpir')


def test_PitchRangeInventoryMaterialPackageMaker_02():
    '''Populate output material module.
    '''

    score_manager = scoremanagertools.scoremanager.ScoreManager()
    assert not score_manager.package_exists('materials.testpir')
    try:
        score_manager.run(user_input=
            'materials maker pitch testpir default '
            'testpir omi add [A0, C8] add [C2, F#5] add [C2, G5] '
            'rm 1 move 1 2 b default '
            'q'
            )
        mpp = scoremanagertools.makers.PitchRangeInventoryMaterialPackageMaker(
            'materials.testpir')
        assert mpp.directory_contents == ['__init__.py', 'output_material.py', 'tags.py']
        pitch_range_inventory = pitchtools.PitchRangeInventory([
            pitchtools.PitchRange('[C2, G5]'), pitchtools.PitchRange('[C2, F#5]')])
        assert mpp.output_material == pitch_range_inventory
    finally:
        score_manager.run(user_input='m testpir del remove default q')
        assert not score_manager.package_exists('materials.testpir')