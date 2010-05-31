from abjad.container import Container
from abjad.note import Note
from abjad.rest import Rest
from abjad.tools import clonewp
from abjad.tools import construct


def contents_by_counts(container, counts, target_type = Note,
   direction = 'big-endian'):
   r'''Fuse `container` contents by `counts` of `target_type` in
   `direction`::

      abjad> staff = Staff(construct.scale(8))
      abjad> fuse.contents_by_counts(staff, [2, 3, 3])
      abjad> f(staff)
      \new Staff {
         c'4
         c'4.
         c'4.
      }

   Raise value error when sum of `counts` does not equal 
   length of `container`::

      abjad> staff = Staff(construct.scale(8))
      abjad> fuse.contents_by_counts(staff, [99, 99, 99])
      ValueError

   Use during rhythmic construction.

   .. todo:: implement 
      ``fuse.contents_by_duration(container, durations, ...)``.

   .. todo:: implement 
         ``fuse.components_by_duration(container, durations, ...)``.

   .. todo:: implement 
      ``fuse.components_by_counts(container, counts, ...)``.
   '''

   ## assert input types
   assert isinstance(container, Container)

   ## assert input values
   if not sum(counts) == len(container):
      raise ValueError('sum of counts must equal length of container.')

   ## find preprolated durations of glommed parts of container
   tokens = clonewp.by_leaf_counts_with_parentage(container, counts)
   durations = [sum([x.duration.preprolated for x in part]) for part in tokens]

   ## construct new notes or rests
   if target_type == Note:
      new_material = construct.notes(
         0, durations, direction = direction)
   elif target_type == Rest:
      new_material = construct.rests(
         durations, direction = direction)
   else:
      raise ValueError('unknown type of material to construct.')

   ## insert new material in container
   container[:] = new_material

   ## return container
   return container
