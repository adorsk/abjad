from abjad.components._Leaf import _Leaf


class Rest(_Leaf):
   '''The Abjad model of a rest.
   '''

   def __init__(self, *args, **kwargs):
      from abjad.tools.resttools._initialize_rest import _initialize_rest
      _initialize_rest(self, _Leaf, *args)
      self._initialize_keyword_values(**kwargs)
   
   ## OVERLOADS ##

   def __len__(self):
      return 0

   def __repr__(self):
      return '%s(%s)' % (self.__class__.__name__, self.duration)

   ## PRIVATE ATTRIBUTES ##

   @property
   def _compact_representation(self):
      return 'r%s' % self.duration

   ## PUBLIC ATTRIBUTES ##

   @property
   def _body(self):
      '''Read-only body of rest.
      '''
      result = ''
      vertical_positioning_pitch = getattr(self, '_vertical_positioning_pitch', None)
      if vertical_positioning_pitch:
         result += str(vertical_positioning_pitch)
      else:
         result += 'r'
      result += str(self.duration)
      if vertical_positioning_pitch:
         result += r' \rest'
      return [result]
