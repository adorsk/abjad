# -*- encoding: utf-8 -*-


def pitch_name_to_pitch_number(pitch_name):
    '''Change `pitch_name` to chromatic pitch number:

    ::

        >>> pitchtools.pitch_name_to_pitch_number("cs''")
        13

    Return integer or float.
    '''
    from abjad.tools import pitchtools

    match = pitchtools.Pitch._pitch_name_regex.match(pitch_name)
    if match is None:
        raise ValueError('\n\tNot chromatic pitch name: "%s".' % pitch_name)

    groups = match.groups()
    diatonic_pitch_class_name, alphabetic_accidental_abbreviation, octave_tick_string = groups
    diatonic_pitch_class_number = pitchtools.diatonic_pitch_class_name_to_diatonic_pitch_class_number(
        diatonic_pitch_class_name)
    pitch_class_number = pitchtools.diatonic_pitch_class_number_to_pitch_class_number(
        diatonic_pitch_class_number)
    accidental = pitchtools.Accidental(alphabetic_accidental_abbreviation)
    octave_number = \
        pitchtools.OctaveIndication(octave_tick_string).octave_number
    pitch_number = 12 * (octave_number - 4)
    pitch_number += pitch_class_number + accidental.semitones

    return pitch_number