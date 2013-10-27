# -*- encoding: utf-8 -*-
from abjad import *
from abjad.tools import pitcharraytools


def test_pitcharraytools_PitchArrayRow_extend_01():

    array = pitcharraytools.PitchArray([[1, 2, 1], [2, 1, 1]])
    array[0].cells[0].pitches.append(0)
    array[0].cells[1].pitches.append(2)
    array[1].cells[2].pitches.append(4)

    '''
    [c'] [d'     ] [  ]
    [         ] [] [e']
    '''

    array[0].extend([1, 1, 1])
    array[1].extend([3])

    '''
    [c'] [d'     ] [  ] [] [] []
    [         ] [] [e'] [            ]
    '''

    assert array[0].dimensions == (1, 7)
    assert array[0].cell_widths == (1, 2, 1, 1, 1, 1)
    assert array[0].pitches == tuple([pitchtools.NamedPitch(x) for x in [0, 2]])

    assert array[1].dimensions == (1, 7)
    assert array[1].cell_widths == (2, 1, 1, 3)
    assert array[1].pitches == tuple([pitchtools.NamedPitch(x) for x in [4]])