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
    def __init__(self, payload, start_segment_identifier, context_name, 
        segment_start_offset, segment_stop_offset, duration):
        duration = durationtools.Duration(duration)
        assert isinstance(start_segment_identifier, str)
        segment_start_offset = durationtools.Offset(segment_start_offset)
        segment_stop_offset = durationtools.Offset(segment_stop_offset)
        assert segment_stop_offset - segment_start_offset == duration
        assert isinstance(context_name, (str, type(None))), repr(context_name)
        self._payload = payload
        self._duration = duration
        self._start_segment_identifier = start_segment_identifier
        self._segment_start_offset = segment_start_offset
        self._segment_stop_offset = segment_stop_offset
        self._context_name = context_name

    ### SPECIAL METHODS ###

    def __eq__(self, expr):
        if isinstance(expr, type(self)):
            for my_value, expr_value in zip(
                self._mandatory_argument_values, expr._mandatory_argument_values):
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
        '''Command context name.
    
        Return string.
        '''
        return self._context_name

    @property
    def duration(self):
        '''Command duration.
            
        Return duration.
        ''' 
        return self._duration

    @property
    def payload(self):
        '''Command resolved value.
        
        Return object.
        ''' 
        return self._payload

    @property
    def segment_start_offset(self):
        '''Command segment start offset.

        Return offset.
        '''
        return self._segment_start_offset

    @property
    def start_segment_identifier(self):
        '''Command start segment identifier.

        Return string or integer.
        '''
        return self._start_segment_identifier

    @property
    def segment_stop_offset(self):
        '''Command segment stop offset.

        Return offset.
        '''
        return self._segment_stop_offset

    @property
    def vector(self):
        '''Command mandatory argument values.

        Return tuple.
        '''
        return self._mandatory_argument_values
