# -*- encoding: utf-8 -*-
from experimental.tools.musicexpressiontools.SingleContextSetExpression \
    import SingleContextSetExpression


class SingleContextDivisionSetExpression(SingleContextSetExpression):
    r'''Single-context division set expression.
    '''

    ### INITIALIZER ###

    def __init__(
        self,
        source_expression=None,
        target_timespan=None,
        scope_name=None,
        fresh=True,
        persist=True,
        truncate=None,
        ):
        assert isinstance(truncate, (bool, type(None)))
        SingleContextSetExpression.__init__(
            self,
            attribute='divisions',
            source_expression=source_expression,
            target_timespan=target_timespan,
            scope_name=scope_name,
            fresh=fresh,
            persist=persist,
            )
        self._truncate = truncate

    ### PUBLIC METHODS ###

    def evaluate(self):
        r'''Evaluate single-context division set expression.

        Returns timespan-delimited single-context division set expression.
        '''
        from experimental.tools import musicexpressiontools
        target_timespan = self._evaluate_anchor_timespan()
        expression = \
            musicexpressiontools.TimespanScopedSingleContextDivisionSetExpression(
            source_expression=self.source_expression,
            target_timespan=target_timespan,
            scope_name=self.scope_name,
            fresh=self.fresh,
            truncate=self.truncate,
            )
        expression._lexical_rank = self._lexical_rank
        return expression
