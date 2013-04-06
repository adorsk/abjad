from experimental.tools import handlertools
from scf import getters
from scf.editors.ArticulationHandlerEditor import ArticulationHandlerEditor
from scf.editors.TargetManifest import TargetManifest


class ReiteratedArticulationHandlerEditor(ArticulationHandlerEditor):

    ### CLASS ATTRIBUTES ###

    target_manifest = TargetManifest(handlertools.ReiteratedArticulationHandler,
        ('articulation_list', None, 'al', getters.get_articulations, False),
        ('minimum_duration', None, 'nd', getters.get_duration, False),
        ('maximum_duration', None, 'xd', getters.get_duration, False),
        ('minimum_written_pitch', None, 'np', getters.get_named_chromatic_pitch, False),
        ('maximum_written_pitch', None, 'xp', getters.get_named_chromatic_pitch, False),
        )