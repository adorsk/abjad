from abjad.tools import labeltools
from experimental.tools.specificationtools.GeneralizedSetExpression import GeneralizedSetExpression


class NoteHeadColorSetExpression(GeneralizedSetExpression):
    '''Note head color set expression.
    '''    

    ### INITIALIZER ###

    def __init__(self, source_expression=None, target_select_expression_inventory=None):
        GeneralizedSetExpression.__init__(self, attribute='note_head_color',
            source_expression=source_expression,
            target_select_expression_inventory=target_select_expression_inventory)

    ### PUBLIC METHODS ###

    def execute_against_score(self, score):
        '''Execute note head color set expression against `score`.
        '''
        from experimental.tools import specificationtools
        color = self.source_expression.payload
        leaves = []
        for target_select_expression in self.target_select_expression_inventory:
            iterable_payload_expression = target_select_expression.evaluate_against_score(score)
            leaves.extend(iterable_payload_expression.payload)
        for leaf in leaves:
            labeltools.color_leaf(leaf, color)
            leaf.override.beam.color = color
            leaf.override.flag.color = color
            leaf.override.stem.color = color