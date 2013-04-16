from abjad.tools import rhythmmakertools
from experimental import *


def test_OutputIncisedRestRhythmMakerEditor_01():

    editor = scoremanagementtools.editors.OutputIncisedRestRhythmMakerEditor()
    editor.run(user_input='1 [8] [2] [3] [4] 32 q', is_autoadvancing=True)

    maker = rhythmmakertools.OutputIncisedRestRhythmMaker([8], [2], [3], [4], 32)

    assert editor.target == maker