from abjad import *


def test_Selection_get_01():

    staff = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 3)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(
        staff)

    r'''
    \new Staff {
        {
            \time 2/8
            c'8
            d'8
        }
        {
            \time 2/8
            e'8
            f'8
        }
        {
            \time 2/8
            g'8
            a'8
        }
    }
    '''

    assert staff[:].get(Measure, 0) is staff[0]
    assert staff[:].get(Measure, 1) is staff[1]
    assert staff[:].get(Measure, 2) is staff[2]


def test_Selection_get_02():

    staff = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 3)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(
        staff)

    assert staff[:].get(Measure, -1) is staff[2]
    assert staff[:].get(Measure, -2) is staff[1]
    assert staff[:].get(Measure, -3) is staff[0]


def test_Selection_get_03():
    '''Read forwards for positive n.
    '''

    staff = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 3)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(staff)

    r'''
    \new Staff {
      {
            \time 2/8
            c'8
            d'8
      }
      {
            \time 2/8
            e'8
            f'8
      }
      {
            \time 2/8
            g'8
            a'8
      }
    }
    '''

    assert staff[:].get(leaftools.Leaf, 0) is staff[0][0]
    assert staff[:].get(leaftools.Leaf, 1) is staff[0][1]
    assert staff[:].get(leaftools.Leaf, 2) is staff[1][0]
    assert staff[:].get(leaftools.Leaf, 3) is staff[1][1]
    assert staff[:].get(leaftools.Leaf, 4) is staff[2][0]
    assert staff[:].get(leaftools.Leaf, 5) is staff[2][1]


def test_Selection_get_04():
    '''Read backwards for negative n.
    '''

    staff = Staff(Measure((2, 8), notetools.make_repeated_notes(2)) * 3)
    pitchtools.set_ascending_named_diatonic_pitches_on_tie_chains_in_expr(staff)

    r'''
    \new Staff {
      {
            \time 2/8
            c'8
            d'8
      }
      {
            \time 2/8
            e'8
            f'8
      }
      {
            \time 2/8
            g'8
            a'8
      }
    }
    '''

    assert staff[:].get(leaftools.Leaf, -1) is staff[2][1]
    assert staff[:].get(leaftools.Leaf, -2) is staff[2][0]
    assert staff[:].get(leaftools.Leaf, -3) is staff[1][1]
    assert staff[:].get(leaftools.Leaf, -4) is staff[1][0]
    assert staff[:].get(leaftools.Leaf, -5) is staff[0][1]
    assert staff[:].get(leaftools.Leaf, -6) is staff[0][0]


def test_Selection_get_05():

    staff = Staff([])
    durations = [Duration(n, 16) for n in range(1, 5)]
    notes = notetools.make_notes([0, 2, 4, 5], durations)
    rests = resttools.make_rests(durations)
    leaves = sequencetools.interlace_sequences(notes, rests)
    staff.extend(leaves)

    r'''
    \new Staff {
        c'16
        r16
        d'8
        r8
        e'8.
        r8.
        f'4
        r4
    }
    '''

    assert staff[:].get(Note, 0) is notes[0]
    assert staff[:].get(Note, 1) is notes[1]
    assert staff[:].get(Note, 2) is notes[2]
    assert staff[:].get(Note, 3) is notes[3]

    assert staff[:].get(Rest, 0) is rests[0]
    assert staff[:].get(Rest, 1) is rests[1]
    assert staff[:].get(Rest, 2) is rests[2]
    assert staff[:].get(Rest, 3) is rests[3]

    assert staff.select().get(Staff, 0) is staff


def test_Selection_get_06():
    '''Iterates backwards with negative values of n.
    '''

    staff = Staff([])
    durations = [Duration(n, 16) for n in range(1, 5)]
    notes = notetools.make_notes([0, 2, 4, 5], durations)
    rests = resttools.make_rests(durations)
    leaves = sequencetools.interlace_sequences(notes, rests)
    staff.extend(leaves)

    r'''
    \new Staff {
        c'16
        r16
        d'8
        r8
        e'8.
        r8.
        f'4
        r4
    }
    '''

    assert staff[:].get(Note, -1) is notes[3]
    assert staff[:].get(Note, -2) is notes[2]
    assert staff[:].get(Note, -3) is notes[1]
    assert staff[:].get(Note, -4) is notes[0]

    assert staff[:].get(Rest, -1) is rests[3]
    assert staff[:].get(Rest, -2) is rests[2]
    assert staff[:].get(Rest, -3) is rests[1]
    assert staff[:].get(Rest, -4) is rests[0]