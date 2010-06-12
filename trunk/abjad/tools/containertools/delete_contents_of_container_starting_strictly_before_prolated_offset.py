from abjad.tools.containertools.get_first_element_starting_strictly_before_prolated_offset \
   import get_first_element_starting_strictly_before_prolated_offset


def delete_contents_of_container_starting_strictly_before_prolated_offset(
   container, prolated_offset):
   r'''.. versionadded:: 1.1.2

   Delete `container` contents starting before `prolated_offset`::

      abjad> staff = Staff(construct.scale(4))
      abjad> Beam(staff.leaves)
      abjad> f(staff)
      \new Staff {
         c'8 [
         d'8
         e'8
         f'8 ]
      }
      
   ::
      
      abjad> containertools.delete_contents_of_container_starting_before_prolated_offset(staff, Rational(1, 8))
      Staff{3}

   ::

      abjad> f(staff)
      \new Staff {
         d'8 [
         e'8
         f'8 ]
      }

   Return `container`.

   .. versionchanged:: 1.1.2
      renamed ``containertools.contents_delete_starting_before_prolated_offset( )`` to
      ``containertools.delete_contents_of_container_starting_strictly_before_prolated_offset( )``.
   '''

   ## get index
   try:
      element = get_first_element_starting_strictly_before_prolated_offset(
         container, prolated_offset)
      index = container.index(element)

   ## return container if no index
   except ValueError:
      return container

   ## delete elements
   del(container[:index+1])

   ## return container
   return container
