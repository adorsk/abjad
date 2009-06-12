from abjad import *


def test_listtools_cumulative_weights_01( ):
   '''Yield signed weights of the cumulative elements in *l*.'''

   l = [1, -2, -3, 4, -5, -6, 7, -8, -9, 10]
   t = list(listtools.cumulative_weights(l))

   assert t == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]


def test_listtools_cumulative_weights_02( ):

   l = [-1, -2, -3, -4, -5, 6, 7, 8, 9, 10]
   t = list(listtools.cumulative_weights(l))

   assert t == [1, 3, 6, 10, 15, 21, 28, 36, 45, 55]


def test_listtools_cumulative_weights_03( ):

   l = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
   t = list(listtools.cumulative_weights(l))

   assert t == [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


def test_listtools_cumulative_weights_04( ):

   l = [1, 2, 3, 4, 5, 0, 0, 0, 0, 0]
   t = list(listtools.cumulative_weights(l))

   assert t == [1, 3, 6, 10, 15, 15, 15, 15, 15, 15]


def test_listtools_cumulative_weights_05( ):

   l = [-1, -2, -3, -4, -5, 0, 0, 0, 0, 0]
   t = list(listtools.cumulative_weights(l))

   assert t == [1, 3, 6, 10, 15, 15, 15, 15, 15, 15]
