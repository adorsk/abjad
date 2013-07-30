def select(expr=None):
    '''Select `expr`.

    Return selection.
    '''
    from abjad.tools import componenttools
    from abjad.tools import selectiontools
    if isinstance(expr, componenttools.Component):
        return selectiontools.ComponentSelection(expr)
    elif hasattr(expr, '_music'):
        music = expr._music
        return selectiontools.ComponentSelection(music)
    elif expr is None:
        return selectiontools.ComponentSelection()
    else:
        return selectiontools.ComponentSelection(expr)