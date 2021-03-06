# -*- encoding: utf-8 -*-
from abjad.tools import datastructuretools
from abjad.tools import instrumenttools
from abjad.tools import pitchtools
from abjad.tools import scoretools
from abjad.tools.agenttools.InspectionAgent import inspect
from experimental.tools.musicexpressiontools.LeafSetExpression \
    import LeafSetExpression


class PitchSetExpression(LeafSetExpression):
    r'''Pitch set expression.
    '''

    ### INITIALIZER ###

    def __init__(
        self, 
        source_expression=None, 
        target_select_expression_inventory=None,
        node_count=None, 
        level=None, 
        trope=None,
        ):
        LeafSetExpression.__init__(
            self,
            source_expression=source_expression,
            target_select_expression_inventory=target_select_expression_inventory,
            )
        assert isinstance(node_count, (int, type(None)))
        assert isinstance(level, (int, type(None)))
        self._node_count = node_count
        self._level = level
        self._trope = trope

    ### PUBLIC PROPERTIES ##

    @property
    def level(self):
        r'''Pitch set expression level.

        Returns integer or none.
        '''
        return self._level

    @property
    def node_count(self):
        r'''Pitch set expression node count.

        Returns nonnegative integer or none.
        '''
        return self._node_count

    @property
    def trope(self):
        r'''Pitch set expression trope.
        '''
        return self._trope

    ### PUBLIC METHODS ###

    def execute_against_score(self, score):
        r'''Execute pitch set expression against `score`.
        '''
        statal_server_cursor = self.source_expression.payload
        leaves = list(self._iterate_selected_leaves_in_score(score))
        assert all(isinstance(leaf, (scoretools.Note, scoretools.Chord)) 
            for leaf in leaves)
        if self.level is None:
            level = -1
        else:
            level = self.level
        if self.node_count is None:
            node_count = len(leaves)
        else:
            node_count = self.node_count
        pitch_numbers = \
            statal_server_cursor(n=node_count, level=level)
        pitch_numbers = \
            datastructuretools.CyclicTuple(pitch_numbers)
        for i, leaf in enumerate(leaves):
            #leaf.sounding_pitch = pitch_numbers[i]
            sounding_pitch = pitch_numbers[i]
            instrument = leaf._get_effective(instrumenttools.Instrument)
            if instrument:
                reference_pitch = instrument.sounding_pitch_of_written_middle_c
            else:
                reference_pitch = pitchtools.NamedPitch('C4')
            t_n = reference_pitch - pitchtools.NamedPitch('C4')
            written_pitch = pitchtools.transpose_pitch_carrier_by_interval(
                    sounding_pitch, t_n)
            leaf.written_pitch = written_pitch
            assert inspect(leaf).get_sounding_pitch() == sounding_pitch
