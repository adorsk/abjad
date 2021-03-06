# -*- encoding: utf-8 -*-
import copy
from abjad.tools import datastructuretools
from abjad.tools import timespantools
from experimental.tools.musicexpressiontools.Expression import Expression


class AnchoredExpression(Expression):
    r'''Anchored expression.
    '''

    ### INITIALIZER ###

    def __init__(self, anchor=None):
        from experimental.tools import musicexpressiontools
        assert isinstance(anchor, 
            (musicexpressiontools.AnchoredExpression, str, type(None)))
        self._anchor = anchor
        self._score_specification = None

    ### SPECIAL METHODS ###

    def __deepcopy__(self, memo):
        r'''Remove score specification and then reattach score specification.
        '''
        from abjad.tools import systemtools
        input_argument_values = \
            systemtools.StorageFormatManager.get_input_argument_values(self)
        result = type(self)(*input_argument_values)
        result._score_specification = self.score_specification
        if hasattr(self, '_lexical_rank'):
            result._lexical_rank = self._lexical_rank
        return result

    ### PRIVATE PROPERTIES ###

    @property
    def _expression_abbreviation(self):
        r'''Form of anchored expression suitable for inclusion in 
        storage format.
        '''
        return self

    ### PRIVATE METHODS ###

    def _evaluate_anchor_timespan(self):
        r'''Evaluate anchor timespan.

        Returns timespan when anchor timespan is evaluable.

        Returns none when anchor timespan is nonevaluable.
        '''
        if isinstance(self.anchor, str):
            return self.root_specification.timespan
        elif self.anchor is None:
            return self.root_specification.timespan
        result = self.anchor.evaluate()
        if result is None:
            return
        #elif isinstance(result, list):
        elif isinstance(result, (list, datastructuretools.TypedList)):
            new_result = []
            for expression in result:
                if hasattr(expression, 'get_timespan'):
                    new_result.append(expression.get_timespan())
                elif hasattr(expression, 'timespan'):
                    new_result.append(expression.timespan)
                elif isinstance(expression.payload[0], timespantools.Timespan):
                    new_result.append(expression.payload[0])
                else:
                    raise TypeError(expression)
            return new_result
        elif hasattr(result, 'get_timespan'):
            return result.get_timespan()
        elif hasattr(result, 'timespan'):
            return result.timespan
        elif isinstance(result.payload[0], timespantools.Timespan):
            return result.payload[0]
        else:
            raise TypeError(result)

    def _set_root_specification(self, root_specification_identifier):
        assert isinstance(root_specification_identifier, (str, type(None)))
        if isinstance(self.anchor, (str, type(None))):
            self._anchor = root_specification_identifier
        else:
            anchor = copy.deepcopy(self.anchor)
            anchor._set_root_specification(root_specification_identifier)
            self._anchor = anchor

    ### PUBLIC PROPERTIES ###

    @property
    def anchor(self):
        r'''Anchored expression anchor.

        Returns none when anchored expression anchors to the entire score.

        Returns string name of segment when anchored expression anchors 
        to a single segment.

        Returns expression when anchored expression anchors 
        to another expression.
        '''
        return self._anchor

    @property
    def is_score_rooted(self):
        r'''Is true when anchored expression is score-rooted.
        Otherwise false.

        Returns boolean.
        '''
        return self.root_specification_identifier is None

    @property
    def is_segment_rooted(self):
        r'''Is true when anchored expression is segment-rooted.
        Otherwise false.

        Returns boolean.
        '''
        return isinstance(self.root_specification_identifier, str)

    @property
    def root_specification(self):
        r'''Anchored expression root specification.

        Returns specification.
        '''
        if self.is_segment_rooted:
            return self.score_specification.segment_specifications[
                self.root_specification_identifier]
        else:
            return self.score_specification

    @property
    def root_specification_identifier(self):
        r'''Anchored expression root identifier.

        Segment-rooted expressions return string.

        Score-rooted expressions return none.
        '''
        if isinstance(self.anchor, (str, type(None))):
            return self.anchor
        else:
            return self.anchor.root_specification_identifier

    @property
    def score_specification(self):
        r'''Anchored expression score specification.

        Returns score specification.
        '''
        return self._score_specification

    @property
    def start_offset(self):
        r'''Anchored expression start offset.

        Returns offset expression.
        '''
        from experimental.tools import musicexpressiontools
        result = musicexpressiontools.OffsetExpression(
            anchor=self._expression_abbreviation)
        result._score_specification = self.score_specification
        return result

    @property
    def stop_offset(self):
        r'''Anchored expression stop offset.

        Returns offset expression.
        '''
        from experimental.tools import musicexpressiontools
        result = musicexpressiontools.OffsetExpression(
            anchor=self._expression_abbreviation, edge=Right)
        result._score_specification = self.score_specification
        return result
