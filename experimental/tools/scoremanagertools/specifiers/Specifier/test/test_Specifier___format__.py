# -*- encoding: utf-8 -*-
from experimental.tools.scoremanagertools.specifiers.Specifier import Specifier
from experimental import *


class ConcreteSpecifier(Specifier):
    @property
    def _one_line_menuing_summary(self):
        pass
    @property
    def _storage_format_specification(self):
        from abjad.tools import systemtools
        return systemtools.StorageFormatSpecification(
            self,
            tools_package_name='specialtools',
            )


def test_Specifier___format___01():
    r'''No keywords.
    '''

    specifier = ConcreteSpecifier()

    assert repr(specifier) == 'ConcreteSpecifier()'
    assert format(specifier) == 'specialtools.ConcreteSpecifier()'


def test_Specifier___format___02():
    r'''With keywords.
    '''

    specifier = ConcreteSpecifier(custom_identifier='foo')

    assert repr(specifier) == "ConcreteSpecifier(custom_identifier='foo')"
    assert systemtools.TestManager.compare(
        format(specifier),
        r'''
        specialtools.ConcreteSpecifier(
            custom_identifier='foo',
            )
        ''',
        )
