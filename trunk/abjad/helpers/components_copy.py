from abjad.exceptions.exceptions import ContiguityError
from abjad.helpers.assert_components import _assert_components
from abjad.helpers.get_parent_and_index import _get_parent_and_index


## TODO: Finish implementation

def components_copy(components):
   '''Deep copy components.
      Copy the portions of all spanners attaching to components.
      Leave components unchanged.
      Return Python list of deep copy of components.

      Example:'''

   # check input
   _assert_components(components, contiguity = 'strict', share = 'score')

   for component in components:

      parent, index = _get_parent_and_index(component) 
