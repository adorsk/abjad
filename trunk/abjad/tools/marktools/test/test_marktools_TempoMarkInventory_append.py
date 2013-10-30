# -*- encoding: utf-8 -*-
from abjad import *


def test_marktools_TempoMarkInventory_append_01():

    tempo_mark_inventory_1 = marktools.TempoMarkInventory([((1, 8), 72)])
    tempo_mark_inventory_1.append(((1, 8), 84))
    tempo_mark_inventory_2 = marktools.TempoMarkInventory([((1, 8), 72), ((1, 8), 84)])

    assert tempo_mark_inventory_1 == tempo_mark_inventory_2