from abjad import *


def test_cfgtools_get_abjad_version_string_01( ):

   assert isinstance(cfgtools.get_abjad_version_string( ), str)
