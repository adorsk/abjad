# -*- encoding: utf-8 -*-
from experimental.tools.scoremanagertools.wizards.HandlerCreationWizard \
    import HandlerCreationWizard


class DynamicHandlerCreationWizard(HandlerCreationWizard):

    ### CLASS VARIABLES ###

    handler_editor_class_name_suffix = 'Editor'

    ### INITIALIZER ###

    def __init__(self, session=None, target=None):
        from experimental.tools.scoremanagertools.iotools import Selector
        HandlerCreationWizard.__init__(
            self,
            session=session,
            target=target,
            )

        selector = Selector.make_dynamic_handler_class_name_selector(
            session=self.session,
            )
        self.selector = selector

    ### PRIVATE PROPERTIES ###

    @property
    def _breadcrumb(self):
        return 'dynamic handler creation wizard'
