# -*- encoding: utf-8 -*-
from experimental import *


def test_TerracedDynamicsHandlerEditor_run_01():

    editor = scoremanagertools.editors.TerracedDynamicsHandlerEditor()
    editor._run(pending_user_input="1 ['p', 'f', 'f'] Duration(1, 8) q", is_autoadvancing=True)

    handler = handlertools.TerracedDynamicsHandler(
        dynamics=['p', 'f', 'f'],
        minimum_duration=Duration(1, 8),
        )

    assert editor.target == handler
