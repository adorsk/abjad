# -*- encoding: utf-8 -*-
from abjad.tools import instrumenttools
from abjad.tools import scoretools
from abjad.tools.instrumenttools.Instrument import Instrument
from experimental.tools.scoremanagertools import getters
from experimental.tools.scoremanagertools import wizards
from experimental.tools.scoremanagertools.editors.ListEditor \
    import ListEditor
from experimental.tools.scoremanagertools.editors.InstrumentEditor \
    import InstrumentEditor
from experimental.tools.scoremanagertools.editors.TargetManifest \
    import TargetManifest


class PerformerEditor(ListEditor):

    ### CLASS VARIABLES ###

    item_class = Instrument

    item_creator_class = wizards.InstrumentCreationWizard

    item_creator_class_kwargs = {'is_ranged': True}

    item_editor_class = InstrumentEditor

    item_identifier = 'instrument'

    target_manifest = TargetManifest(
        instrumenttools.Performer,
        ('name', 'nm', getters.get_string),
        target_attribute_name='name',
        )

    ### PUBLIC PROPERTIES ###

    @property
    def items(self):
        return self.target.instruments

    ### PUBLIC METHODS ###

    def initialize_target(self):
        if self.target is not None:
            return
        else:
            self.target = self.target_class()
