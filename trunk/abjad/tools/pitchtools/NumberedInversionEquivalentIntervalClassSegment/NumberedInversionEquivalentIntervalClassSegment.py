# -*- encoding: utf-8 -*-
from abjad.tools.pitchtools.IntervalClassSegment import IntervalClassSegment


class NumberedInversionEquivalentIntervalClassSegment(IntervalClassSegment):
    '''Abjad model of inversion-equivalent chromatic interval-class segment:

    ::

        >>> pitchtools.NumberedInversionEquivalentIntervalClassSegment(
        ...     [2, 1, 0, 5.5, 6])
        NumberedInversionEquivalentIntervalClassSegment(2, 1, 0, 5.5, 6)

    Inversion-equivalent chromatic interval-class segments are immutable.
    '''

    def __new__(self, interval_class_tokens):
        from abjad.tools import pitchtools
        interval_classes = [
            pitchtools.NumberedInversionEquivalentIntervalClass(x) 
            for x in interval_class_tokens]
        return tuple.__new__(self, interval_classes)

    ### SPECIAL METHODS ###

    def __repr__(self):
        return '%s(%s)' % (self._class_name, self._format_string)

    ### PRIVATE PROPERTIES ###

    @property
    def _format_string(self):
        return ', '.join([str(x) for x in self])