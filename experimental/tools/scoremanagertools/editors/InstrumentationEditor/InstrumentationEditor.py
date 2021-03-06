# -*- encoding: utf-8 -*-
from abjad.tools import instrumenttools
from experimental.tools.scoremanagertools import getters
from experimental.tools.scoremanagertools import wizards
from experimental.tools.scoremanagertools.editors.ListEditor \
    import ListEditor
from experimental.tools.scoremanagertools.editors.PerformerEditor \
    import PerformerEditor
from experimental.tools.scoremanagertools.editors.TargetManifest \
    import TargetManifest


class InstrumentationEditor(ListEditor):

    ### CLASS VARIABLES ###

    item_class = instrumenttools.Performer

    item_creator_class = wizards.PerformerCreationWizard

    item_creator_class_kwargs = {'is_ranged': True}

    item_editor_class = PerformerEditor

    item_identifier = 'performer'

    target_manifest = TargetManifest(
        instrumenttools.InstrumentationSpecifier,
        )

    ### PRIVATE PROPERTIES ###

    @property
    def _breadcrumb(self):
        return self.target_name or 'instrumentation'

    ### PUBLIC PROPERTIES ###

    @property
    def items(self):
        return self.target.performers
