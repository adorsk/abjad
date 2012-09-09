import abc
from abjad.tools import durationtools
from abjad.tools.abctools.AbjadObject import AbjadObject
from experimental import timespaninequalitytools 


class Command(AbjadObject):
    '''.. versionadded:: 1.0

    Abstract command class from which concrete command classes inherit.

    Basically a fancy tuple.
    '''

    ### CLASS ATTRIBUTES ###

    __metaclass__ = abc.ABCMeta

    ### INTIAILIZER ###

    @abc.abstractmethod
    def __init__(self, resolved_value, start_segment_name, context_name, start_offset, stop_offset, duration):
        duration = durationtools.Duration(duration)
        assert isinstance(start_segment_name, str)
        start_offset = durationtools.Offset(start_offset)
        stop_offset = durationtools.Offset(stop_offset)
        assert stop_offset - start_offset == duration, repr((stop_offset, start_offset, duration))
        assert isinstance(context_name, (str, type(None))), repr(context_name)
        self._resolved_value = resolved_value
        self._duration = duration
        self._start_segment_name = start_segment_name
        self._start_offset = start_offset
        self._stop_offset = stop_offset
        self._context_name = context_name

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        if isinstance(expr, type(self)):
            for my_value, expr_value in zip(self._mandatory_argument_values, expr._mandatory_argument_values):
                if not my_value == expr_value:
                    return False
            else:
                return True
        return False

    def __lt__(self, expr):
        return timespaninequalitytools.timespan_2_starts_before_timespan_1_starts(expr, self)

    ### READ-ONLY PUBLIC PROPERTIES ###

    @property
    def context_name(self):
        '''Name of context giving rise to command.
        '''
        return self._context_name

    @property
    def duration(self):
        return self._duration

    @property
    def resolved_value(self):
        return self._resolved_value

    @property
    def start_offset(self):
        return self._start_offset

    @property
    def start_segment_name(self):
        return self._start_segment_name

    @property
    def stop_offset(self):
        return self._stop_offset

    @property
    def vector(self):
        return self._mandatory_argument_values
