from abjad.components import Measure
from abjad.tools.skiptools.Skip import Skip
from abjad.tools import measuretools


def _rational_to_whitespace_measure_string(duration):
   '''Turn rational into whitespace measure string.'''

   ## make measure with hidden staff and hidden time signature
   measure = measuretools.make_rigid_measures_with_full_measure_spacer_skips([duration])[0]
   measure.override.staff.time_signature.stencil = False
   measure.staff.hide = True

   ## return measure string
   return measure.format
