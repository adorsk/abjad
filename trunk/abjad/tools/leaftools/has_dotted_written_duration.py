from abjad.tools import iterate


def has_dotted_written_duration(expr):
   '''.. versionadded:: 1.1.2

   True when at least one of the written durations in `expr`
   carries a rhythmic dot. ::

      abjad> notes = construct.notes([0], [(1, 16), (2, 16), (3, 16)])
      abjad> leaftools.has_dotted_written_duration(notes)
      True
   
   False otherwise. ::

      abjad> notes = construct.notes([0], [(1, 16), (2, 16), (4, 16)])
      abjad> leaftools.has_dotted_written_duration(notes)
      False
   '''

   for leaf in iterate.leaves_forward_in(expr):
      if not leaf.duration.written._numerator == 1:
         return True
   return False
