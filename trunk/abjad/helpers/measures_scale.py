from abjad.measure.measure import _Measure
from abjad.meter.meter import Meter
from abjad.rational.rational import Rational
from abjad.tools import containertools
from abjad.tools import iterate
from abjad.tools import mathtools
from abjad.tools import metertools


def measures_scale(expr, multiplier = Rational(1)):
   '''Iterate expr. For every measure in expr:

         1. multiply measure's meter by multiplier
         2. scale measure's contents to fit new meter

      Extends containertools.contents_scale( ).
      Returns None because iterates possibly many measures.

      This might best be a bound method on RigidMeasure.'''

   for measure in iterate.naive(expr, _Measure):

      if multiplier == Rational(1):
         continue

      if mathtools.is_power_of_two(multiplier) and 1 <= multiplier:
         old_numerator = measure.meter.effective.numerator
         old_denominator = measure.meter.effective.denominator
         new_denominator = old_denominator / multiplier._n
         new_meter = Meter(old_numerator, new_denominator)
      else:
         old_meter = measure.meter.effective
         old_denominator = old_meter.denominator
         old_duration = old_meter.duration
         new_duration = multiplier * old_duration
         new_meter = metertools.make_best(
            new_duration, [old_denominator], multiplier._d)
      measure.meter.forced = new_meter

      contents_multiplier_denominator = mathtools.next_least_power_of_two(multiplier._d)
      contents_multiplier = Rational(
         multiplier._n, contents_multiplier_denominator)
      containertools.contents_scale(measure, contents_multiplier)
