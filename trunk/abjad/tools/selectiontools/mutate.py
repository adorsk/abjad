# -*- encoding: utf-8 -*-


def mutate(expr):
    r'''Wraps `expr` in the Abjad mutation interface.

    Returns mutation interface.
    '''
    from abjad.tools import componenttools
    from abjad.tools import selectiontools
    assert isinstance(expr, componenttools.Component)
    return selectiontools.SingleComponentMutationInterface(expr)
