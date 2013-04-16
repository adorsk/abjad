from experimental import *
from abjad import *
from experimental.tools.scoremanagementtools import specifiers


def test_MusicContributionSpecifierEditor_run_01():

    editor = scoremanagementtools.editors.MusicContributionSpecifierEditor()
    editor.run(user_input='name blue~violin~pizzicati add instrument instrument violin done done')

    specifier = specifiers.MusicContributionSpecifier([
        specifiers.InstrumentSpecifier(
            instrument=instrumenttools.Violin()
            )
        ],
        name='blue violin pizzicati'
        )

    assert editor.target == specifier