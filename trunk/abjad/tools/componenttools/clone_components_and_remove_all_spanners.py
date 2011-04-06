from abjad.tools import spannertools
from abjad.tools.componenttools._ignore_parentage_of_components import _ignore_parentage_of_components
from abjad.tools.componenttools._restore_parentage_to_components_by_receipt import _restore_parentage_to_components_by_receipt
from abjad.tools.marktools._reattach_blinded_marks_to_components_in_expr import _reattach_blinded_marks_to_components_in_expr
import copy


def clone_components_and_remove_all_spanners(components, n = 1):
   r'''Clone thread-contiguous `components` and remove any spanners.
   
   The steps taken by this function are as follows.
   Withdraw all components at any level in `components` from spanners.
   Deep copy unspanned components in `components`.
   Reapply spanners to all components at any level in `components`. ::
   
      abjad> voice = Voice(Measure((2, 8), notetools.make_repeated_notes(2)) * 3)
      abjad> macros.diatonicize(voice)
      abjad> beam = spannertools.BeamSpanner(voice.leaves[:4])
      abjad> f(voice)
      \new Voice {
              {
                      \time 2/8
                      c'8 [
                      d'8
              }
              {
                      \time 2/8
                      e'8
                      f'8 ]
              }
              {
                      \time 2/8
                      g'8
                      a'8
              }
      }

   ::

      abjad> result = componenttools.clone_components_and_remove_all_spanners(voice.leaves[2:4])
      abjad> result
      (Note(e', 8), Note(f', 8))

   ::

      abjad> new_voice = Voice(result)
      abjad> f(new_voice)
      \new Voice {
              e'8
              f'8
      }

   ::

      abjad> voice.leaves[2] is new_voice.leaves[0]
      False

   ::

      abjad> voice.leaves[2].beam.spanner is new_voice.leaves[0].beam.spanner
      False

   Clone `components` a total of `n` times. ::

      abjad> result = componenttools.clone_components_and_remove_all_spanners(voice.leaves[2:4], n = 3)
      abjad> result
      (Note(e', 8), Note(f', 8), Note(e', 8), Note(f', 8), Note(e', 8), Note(f', 8))

   ::

      abjad> new_voice = Voice(result)
      abjad> f(new_voice)
      \new Voice {
              e'8 
              f'8 
              e'8 
              f'8 
              e'8 
              f'8 
      }


   .. versionchanged:: 1.1.2
      renamed ``clone.unspan( )`` to
      ``componenttools.clone_components_and_remove_all_spanners( )``.
   '''
   from abjad.tools import componenttools

   if n < 1:
      return [ ]

   assert componenttools.all_are_thread_contiguous_components(components)

   spanners = spannertools.get_spanners_contained_by_components(components) 
   for spanner in spanners:
      spanner._block_all_components( )

   receipt = _ignore_parentage_of_components(components)

   result = copy.deepcopy(components)
   for component in result:
      #component._update._mark_all_improper_parents_for_update( )
      component._mark_entire_score_tree_for_later_update('prolated')

   _restore_parentage_to_components_by_receipt(receipt)

   for spanner in spanners:
      spanner._unblock_all_components( )

   for i in range(n - 1):
      result += clone_components_and_remove_all_spanners(components)

   _reattach_blinded_marks_to_components_in_expr(result)
      
   return result
