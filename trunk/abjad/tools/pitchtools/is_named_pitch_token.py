# -*- encoding: utf-8 -*-
# TODO: extend with strings like "c" and "A4"
def is_named_pitch_token(pitch_token):
    '''True when `pitch_token` has the form of an Abjad pitch token.
    Otherwise false:

    ::

        >>> pitchtools.is_named_pitch_token(('c', 4))
        True

    Return boolean.
    '''
    from abjad.tools import pitchtools

    if isinstance(pitch_token, pitchtools.NamedPitch):
        return True
    elif pitchtools.is_pitch_class_name_octave_number_pair(pitch_token):
        return True
    elif isinstance(pitch_token, (int, long)):
        return True
    elif isinstance(pitch_token, float) and pitch_token % 0.5 == 0:
        return True
    else:
        return False