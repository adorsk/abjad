# -*- encoding: utf-8 -*-
from experimental import *


def test_ReservoirStartHelperCreationWizard_run_01():

    wizard = scoremanagertools.wizards.ReservoirStartHelperCreationWizard()
    assert wizard._run(pending_user_input='q') == []

    wizard = scoremanagertools.wizards.ReservoirStartHelperCreationWizard()
    assert wizard._run(pending_user_input='b') == []


def test_ReservoirStartHelperCreationWizard_run_02():

    wizard = scoremanagertools.wizards.ReservoirStartHelperCreationWizard()
    assert wizard._run(pending_user_input='start~at~index~0') == [('start at index 0', ())]
