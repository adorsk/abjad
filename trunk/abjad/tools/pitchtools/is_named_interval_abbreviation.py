# -*- encoding: utf-8 -*-


def is_named_interval_abbreviation(expr):
    '''True when `expr` is a melodic diatonic interval abbreviation. Otherwise false:

    ::

        >>> pitchtools.is_named_interval_abbreviation('+M9')
        True

    The regex ``^([+,-]?)(M|m|P|aug|dim)(\d+)$`` underlies this predicate.

    Return boolean.
    '''
    from abjad.tools import pitchtools
    if not isinstance(expr, str):
        return False
    return bool(pitchtools.Interval._interval_name_abbreviation_regex.match(expr))