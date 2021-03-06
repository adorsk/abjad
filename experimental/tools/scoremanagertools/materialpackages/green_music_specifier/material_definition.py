# -*- encoding: utf-8 -*-
from abjad import *
from experimental.tools.scoremanagertools import specifiers
output_material_module_import_statements = [
    'from abjad import *',
    'from experimental.tools.scoremanagertools import specifiers',
    ]


green_music_specifier = specifiers.MusicSpecifier([
    specifiers.MusicContributionSpecifier(
        [specifiers.InstrumentSpecifier(instrument=instrumenttools.Violin())],
        custom_identifier='green violin pizzicati',
        description='upper register violin pizzicati'
        )
    ],
    custom_identifier='green music'
    )
