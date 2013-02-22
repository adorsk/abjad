from abjad.tools import notetools
from abjad.tools import pitchtools
from experimental.tools.specificationtools.GeneralizedSetExpression import GeneralizedSetExpression


class AggregateSetExpression(GeneralizedSetExpression):
    '''Aggregate set expression.
    '''

    ### INITIALIZER ###

    def __init__(self, source_expression=None, target_select_expression_inventory=None):
        GeneralizedSetExpression.__init__(self, attribute='aggregate',
            source_expression=source_expression,
            target_select_expression_inventory=target_select_expression_inventory)

    ### PUBLIC METHODS ###

    def execute_against_score(self, score):
        '''Execute aggregate set expression against `score`.
        '''
        from experimental.tools import specificationtools
        aggregate = self.source_expression.payload
        leaves = []
        for target_select_expression in self.target_select_expression_inventory:
            iterable_payload_expression = target_select_expression.evaluate_against_score(score)
            leaves.extend(iterable_payload_expression.payload)
        for leaf in leaves:
            assert isinstance(leaf, notetools.Note), repr(leaf)
            sounding_pitches = \
                pitchtools.register_chromatic_pitch_class_numbers_by_chromatic_pitch_number_aggregate(
                [leaf.sounding_pitch.chromatic_pitch_number], aggregate)
            leaf.sounding_pitch = sounding_pitches[0]