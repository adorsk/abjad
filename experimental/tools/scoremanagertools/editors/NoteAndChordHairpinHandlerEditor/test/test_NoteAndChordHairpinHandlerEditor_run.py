# -*- encoding: utf-8 -*-
from experimental import *


def test_NoteAndChordHairpinHandlerEditor_run_01():

    editor = scoremanagertools.editors.NoteAndChordHairpinHandlerEditor()
    editor._run(pending_user_input="1 ('p', '<', 'f') Duration(1, 8) q", is_autoadvancing=True)

    handler = handlertools.NoteAndChordHairpinHandler(
        hairpin_token=('p', '<', 'f'),
        minimum_duration=Duration(1, 8),
        )

    assert editor.target == handler
