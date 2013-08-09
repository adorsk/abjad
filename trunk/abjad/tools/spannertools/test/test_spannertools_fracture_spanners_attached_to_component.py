# -*- encoding: utf-8 -*-
from abjad import *


def test_spannertools_fracture_spanners_attached_to_component_01():

    staff = Staff("c'8 d'8 e'8 f'8")
    beam = spannertools.BeamSpanner(staff.select_leaves())
    slur = spannertools.SlurSpanner(staff.select_leaves())
    trill = spannertools.TrillSpanner(staff)

    r'''
    \new Staff {
        c'8 [ ( \startTrillSpan
        d'8
        e'8
        f'8 ] ) \stopTrillSpan
    }
    '''

    spannertools.fracture_spanners_attached_to_component(staff[1], direction=Right)

    r'''
    \new Staff {
        c'8 [ ( \startTrillSpan
        d'8 ] )
        e'8 [ (
        f'8 ] ) \stopTrillSpan
    }
    '''

    assert select(staff).is_well_formed()
    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            c'8 [ ( \startTrillSpan
            d'8 ] )
            e'8 [ (
            f'8 ] ) \stopTrillSpan
        }
        '''
        )


def test_spannertools_fracture_spanners_attached_to_component_02():
    r'''With spanner classes filter.
    '''

    staff = Staff("c'8 d'8 e'8 f'8")
    beam = spannertools.BeamSpanner(staff.select_leaves())
    slur = spannertools.SlurSpanner(staff.select_leaves())
    trill = spannertools.TrillSpanner(staff)

    r'''
    \new Staff {
        c'8 [ ( \startTrillSpan
        d'8
        e'8
        f'8 ] ) \stopTrillSpan
    }
    '''

    spanner_classes = (spannertools.BeamSpanner, )
    spannertools.fracture_spanners_attached_to_component(
        staff[1], direction=Right, spanner_classes=spanner_classes)

    r'''
    \new Staff {
        c'8 [ ( \startTrillSpan
        d'8 ]
        e'8 [
        f'8 ] ) \stopTrillSpan
    }
    '''

    assert select(staff).is_well_formed()
    assert testtools.compare(
        staff,
        r'''
        \new Staff {
            c'8 [ ( \startTrillSpan
            d'8 ]
            e'8 [
            f'8 ] ) \stopTrillSpan
        }
        '''
        )
