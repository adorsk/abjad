# -*- encoding: utf-8 -*-
from experimental import *


def test_OctaveTranspositionMappingComponentEditor_run_01():

    editor = scoremanagertools.editors.OctaveTranspositionMappingComponentEditor()
    editor._run(pending_user_input='source [A0, C8] target -18 q')

    assert editor.target == pitchtools.OctaveTranspositionMappingComponent('[A0, C8]', -18)
