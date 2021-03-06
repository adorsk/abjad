# -*- encoding: utf-8 -*-
from experimental.tools.scoremanagertools.predicates import predicates


def test_predicates_01():

    assert predicates.is_available_snake_case_package_name('asdf')
    assert predicates.is_available_snake_case_package_name('scoremanagertools.asdf')
    assert predicates.is_available_snake_case_package_name(
        'experimental.tools.scoremanagertools.materialpackages.asdf')

    assert not predicates.is_available_snake_case_package_name('scoremanagertools')
    assert not predicates.is_available_snake_case_package_name(
        'experimental.tools.scoremanagertools.materialpackages')


def test_predicates_02():

    assert predicates.is_existing_package_name('scoremanagertools')
    assert predicates.is_existing_package_name(
        'experimental.tools.scoremanagertools.materialpackages')

    assert not predicates.is_existing_package_name('asdf')
    assert not predicates.is_existing_package_name('scoremanagertools.asdf')
    assert not predicates.is_existing_package_name(
        'experimental.tools.scoremanagertools.materialpackages.asdf')



def test_predicates_03():

    assert predicates.is_boolean(True)
    assert predicates.is_boolean(False)

    assert not predicates.is_boolean(None)
    assert not predicates.is_boolean('')
    assert not predicates.is_boolean(0)
    assert not predicates.is_boolean(1)
