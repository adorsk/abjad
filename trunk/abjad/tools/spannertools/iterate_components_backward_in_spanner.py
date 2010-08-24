from abjad.components._Component import _Component
from abjad.tools.spannertools.Spanner import Spanner


def iterate_components_backward_in_spanner(spanner, klass = _Component):
   '''.. versionadded:: 1.1.2

   Yield components in `spanner` one at a time from left to right. ::

      abjad> t = Staff(macros.scale(4))
      abjad> p = spannertools.BeamSpanner(t[2:])
      abjad> notes = spannertools.iterate_components_backward_in_spanner(p, class = Note)
      abjad> for note in notes:
         print note
      Note(f', 8)
      Note(e', 8)

   .. versionchanged:: 1.1.2
      renamed ``spannertools.iterate_components_backward( )`` to
      ``spannertools.iterate_components_backward_in_spanner( )``.
   '''
   from abjad.tools import componenttools

   if not isinstance(spanner, Spanner):
      raise TypeError

   for component in reversed(spanner._components):
      dfs = componenttools.iterate_components_depth_first(component, direction = 'right')
      for node in dfs: 
         if isinstance(node, klass):
            yield node
