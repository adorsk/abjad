# -*- encoding: utf-8 -*-
from abjad.tools.pitchtools.NamedIntervalClass import NamedIntervalClass


class NamedHarmonicIntervalClass(NamedIntervalClass):
    '''Abjad model harmonic diatonic interval-class:

    ::

        >>> pitchtools.NamedHarmonicIntervalClass('-M9')
        NamedHarmonicIntervalClass('M2')

    Harmonic diatonic interval-classes are immutable.
    '''

    def __init__(self, *args):
        from abjad.tools.pitchtools.is_melodic_diatonic_interval_abbreviation \
            import melodic_diatonic_interval_abbreviation_regex
        from abjad.tools import pitchtools
        if len(args) == 1:
            if isinstance(args[0], pitchtools.NamedHarmonicInterval):
                quality_string = args[0]._quality_string
                number = args[0].number
            elif isinstance(args[0], str):
                match = \
                    melodic_diatonic_interval_abbreviation_regex.match(args[0])
                if match is None:
                    message = '"%s" does not have the form'
                    message += ' of an hdic abbreviation.'
                    raise ValueError(message % args[0])
                direction_string, quality_abbreviation, number_string = \
                    match.groups()
                quality_string = \
                    NamedIntervalClass._quality_abbreviation_to_quality_string[
                        quality_abbreviation]
                number = int(number_string)
            elif isinstance(args[0], tuple) and len(args[0]) == 2:
                quality_string, number = args[0]
            else:
                raise TypeError
        else:
            quality_string, number = args
        if quality_string not in \
            NamedIntervalClass._acceptable_quality_strings:
            raise ValueError('not acceptable quality string.')
        self._quality_string = quality_string
        if not isinstance(number, int):
            raise TypeError('must be integer.')
        if number == 0:
            raise ValueError('must be nonzero.')
        abs_number = abs(number)
        if abs_number % 7 == 1 and 8 <= abs_number:
            number = 8
        else:
            number = abs_number % 7
            if number == 0:
                number = 7
        self._number = number

    ### SPECIAL METHODS ###

    def __eq__(self, arg):
        if isinstance(arg, type(self)):
            if self._quality_string == arg._quality_string:
                if self.number == arg.number:
                    return True
        return False

    def __ne__(self, arg):
        return not self == arg

    def __str__(self):
        return '%s%s' % (self._quality_abbreviation, self.number)

    ### PRIVATE PROPERTIES ###

    @property
    def _full_name(self):
        return '%s %s' % (self._quality_string, self._interval_string)

    ### PUBLIC METHODS ###

    @classmethod
    def from_pitch_carriers(cls, pitch_carrier_1, pitch_carrier_2):
        '''Calculate harmonic diatonic interval-class from `pitch_carrier_1` to
        `pitch_carrier_2`:

        ::

            >>> pitchtools.NamedHarmonicIntervalClass.from_pitch_carriers(
            ...     pitchtools.NamedPitch(-2), 
            ...     pitchtools.NamedPitch(12),
            ...     )
            NamedHarmonicIntervalClass('M2')

        Return harmonic diatonic interval-class.
        '''
        from abjad.tools import pitchtools
        # get melodic diatonic interval
        mdi = pitchtools.NamedMelodicInterval.from_pitch_carriers(
            pitch_carrier_1, pitch_carrier_2)
        # return harmonic diatonic interval-class
        return mdi.harmonic_diatonic_interval.harmonic_diatonic_interval_class

    def invert(self):
        r'''Inversion of harmonic diatonic interval-class:

        ::

            >>> hdic = pitchtools.NamedHarmonicIntervalClass('major', -9)
            >>> hdic.invert()
            NamedHarmonicIntervalClass('m7')

        Return harmonic diatonic interval-class.
        '''
        from abjad.tools import pitchtools
        low = pitchtools.NamedPitch('c', 4)
        quality_string, number = self._quality_string, self.number
        mdi = pitchtools.NamedMelodicInterval(quality_string, number)
        middle = low + mdi
        octave = pitchtools.NamedMelodicInterval('perfect', 8)
        high = low + octave
        hdi = pitchtools.NamedHarmonicIntervalClass.from_pitch_carriers(
            middle, high)
        return hdi