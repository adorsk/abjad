import copy
from abjad.tools import *
from experimental.tools import library
from experimental.tools import expressiontools
from experimental.tools.specificationtools.Interpreter import Interpreter


class ConcreteInterpreter(Interpreter):
    r'''Concrete interpreter.

    Currently the only interpreter implemented.

    The name is provisional.
    '''

    ### INITIALIZER ###

    def __call__(self, score_specification):
        '''Top-level interpretation entry point::

            * interpret all time signatures scorewide
            * interpret all divisions scorewide
            * interpret all rhythms scorewide
            * interpret all pitch-classes scorewide
            * interpret all registration scorewide
            * interpret all additional parameters scorewide

        Return Abjad score object.
        '''
        Interpreter.__call__(self, score_specification)
        self.interpret_time_signatures()
        self.interpret_divisions()
        self.interpret_rhythm()
        self.interpret_pitch_classes()
        self.interpret_registration()
        self.interpret_additional_parameters()
        return self.score

    def __init__(self):
        pass

    ### PUBLIC METHODS ###

    def add_division_lists_to_score(self):
        for voice in iterationtools.iterate_voices_in_expr(self.score):
            voice_division_list = expressiontools.DivisionList([], voice_name=voice.name)
            voice_proxy = self.score_specification.payload_expressions_by_voice[voice.name]
            expressions = voice_proxy.division_payload_expressions
            divisions = [x.payload.divisions for x in expressions]
            divisions = sequencetools.flatten_sequence(divisions, depth=1)
            start_offset = durationtools.Offset(0)
            for division in divisions:
                division = copy.deepcopy(division)
                division._start_offset = durationtools.Offset(start_offset)
                start_offset += division.duration
                voice_division_list.divisions.append(division)
            voice_proxy._voice_division_list = voice_division_list

    def add_rhythms_to_score(self):
        for voice in iterationtools.iterate_voices_in_expr(self.score):
            voice_proxy = self.score_specification.payload_expressions_by_voice[voice.name]
            for rhythm_payload_expression in voice_proxy.rhythm_payload_expressions:
                voice.extend(rhythm_payload_expression.payload)

    def add_time_signatures_to_score(self):
        single_context_time_signature_set_expressions = \
            self.score_specification.single_context_time_signature_set_expressions[:]
        while single_context_time_signature_set_expressions:
            for single_context_time_signature_set_expression in \
                single_context_time_signature_set_expressions[:]:
                time_signatures = single_context_time_signature_set_expression.make_time_signatures()
                if time_signatures:
                    single_context_time_signature_set_expressions.remove(
                        single_context_time_signature_set_expression)
        time_signatures = self.score_specification.time_signatures
        measures = measuretools.make_measures_with_full_measure_spacer_skips(time_signatures)
        context = componenttools.get_first_component_in_expr_with_name(self.score, 'TimeSignatureContext')
        context.extend(measures)

    def calculate_score_and_segment_timespans(self):
        if hasattr(self.score_specification, '_time_signatures'):
            time_signatures = self.score_specification.time_signatures
            score_duration = sum([durationtools.Duration(x) for x in time_signatures])
            score_start_offset = durationtools.Offset(0)
            score_stop_offset = durationtools.Offset(score_duration)
            self.score_specification._start_offset = durationtools.Offset(0)
            self.score_specification._stop_offset = durationtools.Offset(score_duration)
            score_timespan = timespantools.Timespan(score_start_offset, score_stop_offset)
            self.score_specification._timespan = score_timespan
        else:
            segment_durations = [durationtools.Duration(sum(x.time_signatures)) 
                for x in self.score_specification.segment_specifications]
            assert sequencetools.all_are_numbers(segment_durations)
            score_duration = sum(segment_durations)
            score_start_offset = durationtools.Offset(0)
            score_stop_offset = durationtools.Offset(score_duration)
            self.score_specification._start_offset = durationtools.Offset(0)
            self.score_specification._stop_offset = durationtools.Offset(score_duration)
            score_timespan = timespantools.Timespan(score_start_offset, score_stop_offset)
            self.score_specification._timespan = score_timespan
            segment_offset_pairs = mathtools.cumulative_sums_zero_pairwise(segment_durations)
            segment_offset_pairs = [
                (durationtools.Offset(x[0]), durationtools.Offset(x[1])) for x in segment_offset_pairs]
            for segment_offset_pair, segment_specification in zip(
                segment_offset_pairs, self.score_specification.segment_specifications):
                start_offset, stop_offset = segment_offset_pair
                segment_specification._start_offset = start_offset
                segment_specification._stop_offset = stop_offset
                timespan = timespantools.Timespan(start_offset, stop_offset)
                segment_specification._timespan = timespan

    def interpret_additional_parameters(self):
        pass

    def interpret_divisions(self):
        self.make_timespan_scoped_single_context_set_expressions('divisions')
        self.make_region_expressions('divisions')
        self.make_payload_expressions('divisions')
        self.add_division_lists_to_score()

    def interpret_pitch_classes(self):
        pass

    def interpret_registration(self):
        pass

    def interpret_rhythm(self):
        self.make_timespan_scoped_single_context_set_expressions('rhythm')
        self.make_region_expressions('rhythm')
        #self._debug_values(self.score_specification.rhythm_region_expressions, 'rrxs')
        self.make_payload_expressions('rhythm')
        self.add_rhythms_to_score()

    def interpret_time_signatures(self):
        self.populate_single_context_time_signature_set_expressions()
        self.add_time_signatures_to_score()
        self.calculate_score_and_segment_timespans()

    def make_division_region_expressions_for_voice(self, voice_name):
        voice_proxy = self.score_specification.single_context_set_expressions_by_context[voice_name]
        set_expressions = voice_proxy.timespan_scoped_single_context_division_set_expressions[:]
        region_expressions = []
        for set_expression in set_expressions:
            region_expression = set_expression.evaluate(voice_name)
            region_expressions.append(region_expression)
        return region_expressions

    def make_payload_expressions(self, attribute):
        attribute = attribute.rstrip('s')
        region_expression_key = '{}_region_expressions'.format(attribute)
        payload_expression_key = '{}_payload_expressions'.format(attribute)
        score_region_expressions = getattr(self.score_specification, region_expression_key)
        score_region_expressions = score_region_expressions[:]
        while score_region_expressions:
            made_progress = False
            for region_expression in score_region_expressions[:]:
                assert isinstance(region_expression, expressiontools.RegionExpression)
                payload_expression = region_expression.evaluate()
                if payload_expression is not None:
                    assert isinstance(payload_expression, expressiontools.StartPositionedPayloadExpression)
                    made_progress = True
                    score_region_expressions.remove(region_expression)
                    voice_name = region_expression.voice_name
                    voice_proxy = self.score_specification.payload_expressions_by_voice[voice_name]
                    voice_payload_expressions = getattr(voice_proxy, payload_expression_key)
                    voice_payload_expressions = voice_payload_expressions - payload_expression.timespan
                    voice_payload_expressions.append(payload_expression)
                    voice_payload_expressions.sort()
            if not made_progress:
                raise Exception('cyclic specification.')

    def make_region_expressions(self, attribute):
        attribute = attribute.rstrip('s')
        method_key = 'make_{}_region_expressions_for_voice'.format(attribute)
        score_region_expressions_key = '{}_region_expressions'.format(attribute)
        score_region_expressions = getattr(self.score_specification, score_region_expressions_key)
        for voice in iterationtools.iterate_voices_in_expr(self.score):
            region_expressions = getattr(self, method_key)(voice.name)
            score_region_expressions.extend(region_expressions)

    def make_rhythm_region_expressions_for_voice(self, voice_name):
        voice_proxy = self.score_specification.single_context_set_expressions_by_context[voice_name]
        voice_division_list = self.score_specification.payload_expressions_by_voice[
            voice_name].voice_division_list
        division_payload_expressions = self.score_specification.payload_expressions_by_voice[
            voice_name].division_payload_expressions
        timespan_scoped_single_context_rhythm_set_expressions = \
            voice_proxy.timespan_scoped_single_context_rhythm_set_expressions
        #self._debug_values(timespan_scoped_single_context_rhythm_set_expressions, 'tsscrsxs')
        if not voice_division_list:
            return []
        division_region_durations = [x.timespan.duration for x in division_payload_expressions]
        timespan_scoped_single_context_rhythm_set_expression_durations = [
            x.target_timespan.duration for x in timespan_scoped_single_context_rhythm_set_expressions]
        assert sum(division_region_durations) == \
            sum(timespan_scoped_single_context_rhythm_set_expression_durations)
        timespan_scoped_single_context_rhythm_set_expression_merged_durations = \
            sequencetools.merge_duration_sequences(
            division_region_durations, timespan_scoped_single_context_rhythm_set_expression_durations)
        # assert that rhythm set expressions cover rhythm regions exactly
        assert sequencetools.partition_sequence_by_weights_exactly(
            timespan_scoped_single_context_rhythm_set_expression_merged_durations, 
            timespan_scoped_single_context_rhythm_set_expression_durations)
        rhythm_region_start_division_duration_lists = \
                sequencetools.partition_sequence_by_backgrounded_weights(
                voice_division_list.divisions, 
                timespan_scoped_single_context_rhythm_set_expression_merged_durations)
        #self._debug_values(rhythm_region_start_division_duration_lists, 'rrsddls')
        assert len(rhythm_region_start_division_duration_lists) == \
            len(timespan_scoped_single_context_rhythm_set_expression_merged_durations)
        rhythm_region_start_division_counts = [len(l) for l in rhythm_region_start_division_duration_lists]
        rhythm_region_division_lists = sequencetools.partition_sequence_by_counts(
            voice_division_list.divisions, rhythm_region_start_division_counts, cyclic=False, overhang=False)
        rhythm_region_division_lists = [
            expressiontools.DivisionList(x, voice_name=voice_name) for x in rhythm_region_division_lists]
        assert len(rhythm_region_division_lists) == \
            len(timespan_scoped_single_context_rhythm_set_expression_merged_durations)
        #self._debug_values(rhythm_region_division_lists, 'rrdls')
        rhythm_region_durations = [x.duration for x in rhythm_region_division_lists]
        #self._debug(rhythm_region_durations, 'rrds')
        cumulative_sums = mathtools.cumulative_sums_zero(rhythm_region_durations)
        rhythm_region_start_offsets = cumulative_sums[:-1]
        rhythm_region_start_offsets = [durationtools.Offset(x) for x in rhythm_region_start_offsets]
        timespan_scoped_single_context_rhythm_set_expression_duration_pairs = [
            (x, x.target_timespan.duration) for x in timespan_scoped_single_context_rhythm_set_expressions]
        #self._debug_values(timespan_scoped_single_context_rhythm_set_expression_duration_pairs, 
        #    'rhythm expression / duration pairs')
        merged_duration_timespan_scoped_single_context_rhythm_set_expression_pairs = \
            sequencetools.pair_duration_sequence_elements_with_input_pair_values(
            timespan_scoped_single_context_rhythm_set_expression_merged_durations, 
            timespan_scoped_single_context_rhythm_set_expression_duration_pairs)
        # the first column in pairs is not used for anything further at all is discarded
        timespan_scoped_single_context_rhythm_set_expressions = [
            x[-1] for x in merged_duration_timespan_scoped_single_context_rhythm_set_expression_pairs]
        assert len(timespan_scoped_single_context_rhythm_set_expressions) == len(rhythm_region_division_lists)
        rhythm_region_expressions = []
        for timespan_scoped_single_context_rhythm_set_expression, \
            rhythm_region_start_offset, rhythm_region_division_list in zip(
            timespan_scoped_single_context_rhythm_set_expressions, 
            rhythm_region_start_offsets, rhythm_region_division_lists):
            #self._debug(timespan_scoped_single_context_rhythm_set_expression, 'tsscrsx')
            rhythm_region_expression = timespan_scoped_single_context_rhythm_set_expression.evaluate(
                rhythm_region_division_list, rhythm_region_start_offset, voice_name)
            rhythm_region_expressions.append(rhythm_region_expression)
        #self._debug_values(rhythm_region_expressions, 'rrxs')
        rhythm_region_expressions = self.merge_prolonging_rhythm_region_expressions(
            rhythm_region_expressions)
        #self._debug_values(rhythm_region_expressions, 'rrxs')
        return rhythm_region_expressions

    def make_timespan_scoped_single_context_set_expressions(self, attribute):
        attribute_key = 'timespan_scoped_single_context_{}_set_expressions'.format(attribute.rstrip('s'))
        for voice in iterationtools.iterate_voices_in_expr(self.score):
            timespan_scoped_single_context_set_expressions = \
                self.score_specification.make_timespan_scoped_single_context_set_expressions_for_voice(
                attribute, voice.name)
            #if 'division' in attribute_key:
            #    self._debug_values(timespan_scoped_single_context_set_expressions, 'TTT')
            timespan_scoped_single_context_set_expressions.sort_and_split_set_expressions()
            timespan_scoped_single_context_set_expressions.compute_logical_or()
            timespan_scoped_single_context_set_expressions.supply_missing_set_expressions(
                attribute, self.score_specification, voice.name)
            voice_proxy = self.score_specification.single_context_set_expressions_by_context[voice.name]
            inventory = getattr(voice_proxy, attribute_key)
            inventory[:] = timespan_scoped_single_context_set_expressions[:]
            #if 'division' in attribute_key:
            #    self._debug_values(inventory, 'inventory')
                        
    def merge_prolonging_rhythm_region_expressions(self, rhythm_region_expressions):
        result = []
        for rhythm_region_expression in rhythm_region_expressions:
            if result and isinstance(
                rhythm_region_expression, expressiontools.SelectExpressionRhythmRegionExpression) and \
                rhythm_region_expression.prolongs_expr(result[-1]):
                current_stop_offset = rhythm_region_expression.start_offset
                current_stop_offset += rhythm_region_expression.total_duration
                previous_stop_offset = result[-1].start_offset + result[-1].total_duration
                extra_duration = current_stop_offset - previous_stop_offset
                assert 0 <= extra_duration
                result[-1]._total_duration += extra_duration
            else:
                result.append(rhythm_region_expression)
        return result

    def populate_single_context_time_signature_set_expressions(self):
        score_proxy = self.score_specification.single_context_set_expressions_by_context.score_proxy
        single_context_time_signature_set_expressions = \
            score_proxy.single_context_set_expressions_by_attribute.get('time_signatures', [])
        if single_context_time_signature_set_expressions:
            single_context_time_signature_set_expression = single_context_time_signature_set_expressions[-1]
            self.score_specification.single_context_time_signature_set_expressions.append(
                single_context_time_signature_set_expression)
            return
        for segment_specification in self.score_specification.segment_specifications:
            score_proxy = segment_specification.single_context_set_expressions_by_context.score_proxy
            single_context_time_signature_set_expressions = \
                score_proxy.single_context_set_expressions_by_attribute.get('time_signatures', [])
            if not single_context_time_signature_set_expressions:
                continue
            single_context_time_signature_set_expression = single_context_time_signature_set_expressions[-1]
            self.score_specification.single_context_time_signature_set_expressions.append(
                single_context_time_signature_set_expression)