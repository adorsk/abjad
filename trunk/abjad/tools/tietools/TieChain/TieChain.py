from abjad.tools.abctools.ScoreSelection import ScoreSelection


class TieChain(ScoreSelection):
    '''.. versionadded:: 2.9

    All the notes in a tie chain::

        abjad> staff = Staff("c' d' e' ~ e'")

    ::

        abjad> tietools.get_tie_chain(staff[2])
        TieChain((Note("e'4"), Note("e'4")))

    Tie chains are immutable score selections.
    '''

    def __init__(self, music):
        ScoreSelection.__init__(self, music)

    ### READ-ONLY PROPERTIES ###

    @property
    def head(self):
        '''Read-only reference to element ``0`` in tie chain.
        '''
        if self.music:
            return self.music[0]

    @property
    def is_trivial(self):
        '''True when length of tie chain is less than or equal to ``1``.

        Return boolean.
        '''
        return len(self) <= 1

    @property
    def prolated_duration(self):
        '''Sum of prolated durations of all components in tie chain.
        '''
        return sum([x.prolated_duration for x in self])
