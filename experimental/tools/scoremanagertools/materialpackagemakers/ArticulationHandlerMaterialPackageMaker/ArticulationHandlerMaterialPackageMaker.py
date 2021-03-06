# -*- encoding: utf-8 -*-
from experimental.tools.handlertools.ArticulationHandler \
    import ArticulationHandler
from experimental.tools.scoremanagertools.materialpackagemakers.MaterialPackageMaker \
    import MaterialPackageMaker
from experimental.tools.scoremanagertools.wizards.ArticulationHandlerCreationWizard \
    import ArticulationHandlerCreationWizard


class ArticulationHandlerMaterialPackageMaker(MaterialPackageMaker):

    ### CLASS VARIABLES ###

    generic_output_name = 'articulation handler'

    output_material_checker = staticmethod(
        lambda x: isinstance(x, ArticulationHandler))

    @staticmethod
    def output_material_editor(target=None, session=None):
        from experimental.tools import scoremanagertools
        if target:
            wizard = \
                scoremanagertools.wizards.ArticulationHandlerCreationWizard()
            articulation_handler_editor = wizard.get_handler_editor(
                target.__class__.__name__, target=target)
            return articulation_handler_editor

    output_material_maker = ArticulationHandlerCreationWizard

    output_material_module_import_statements = [
        'from abjad.tools import durationtools',
        'from abjad.tools import pitchtools',
        'from experimental.tools import handlertools',
        ]
