from abjad import *


def test_GraceContainer_parentage_01():
    '''Lone grace container carrier is none.
    '''

    t = leaftools.GraceContainer(notetools.make_repeated_notes(4))
    assert t._carrier is None


def test_GraceContainer_parentage_02():
    '''Grace containers bound to leaf do have parent.
    '''

    t = Note(1, (1, 4))
    leaftools.GraceContainer()(t)
    assert isinstance(t.grace, leaftools.GraceContainer)
    assert t.grace._carrier is t
    assert t.grace._carrier is t


def test_GraceContainer_parentage_03():
    '''Grace containers bound to leaf have their correct carrier after assignment.
    '''

    t = Note(1, (1, 4))
    leaftools.GraceContainer([Note(4, (1, 16))], kind = 'after')(t)
    leaftools.GraceContainer([Note(4, (1, 16))], kind = 'grace')(t)
    assert t.after_grace._carrier is t
    assert t.grace._carrier is t
    t.after_grace[:] = []
    notes = [Note("c'8"), Note("d'8")]
    t.after_grace.extend(notes)
    t.grace[:] = []
    notes = [Note("c'8"), Note("d'8")]
    t.grace.extend(notes)
    assert t.after_grace._carrier is t
    assert t.grace._carrier is t
    t.after_grace[:] = []
    t.grace[:] = []
    assert t.after_grace._carrier is t
    assert t.grace._carrier is t