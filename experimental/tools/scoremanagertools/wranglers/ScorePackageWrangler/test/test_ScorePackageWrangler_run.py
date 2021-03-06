# -*- encoding: utf-8 -*-
import pytest
from experimental import *


def test_ScorePackageWrangler_run_01():
    r'''Create score package. Remove score package.
    '''
    pytest.skip('unskip after deciding about cache.')

    score_manager = scoremanagertools.scoremanager.ScoreManager()
    assert not score_manager.configuration.packagesystem_path_exists('testscore')

    try:
        score_manager._run(pending_user_input=
            'new Test~score testscore 2012 '
            'q'
            )
        assert score_manager.configuration.packagesystem_path_exists('testscore')
        spp = scoremanagertools.managers.ScorePackageManager('testscore')
        assert spp.annotated_title == 'Test score (2012)'
        assert spp.composer is None
        assert spp.instrumentation is None
    finally:
        score_manager._run(pending_user_input='test removescore clobberscore remove default q')
        assert not score_manager.configuration.packagesystem_path_exists('testscore')
