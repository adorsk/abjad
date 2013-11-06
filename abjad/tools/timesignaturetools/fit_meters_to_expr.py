# -*- encoding: utf-8 -*-
from abjad.tools import durationtools
from abjad.tools import datastructuretools


def fit_meters_to_expr(
    expr,
    meters,
    discard_final_orphan_downbeat=True,
    starting_offset=None,
    denominator=32,
    ):
    r'''Find the best-matching sequence of meters for the offsets
    contained in `expr`.

    ::

        >>> meters = [
        ...     timesignaturetools.Meter(x)
        ...     for x in [(3, 4), (4, 4), (5, 4)]]

    ..  container:: example

        **Example 1.** Matching a series of hypothetical 4/4 measures:

        ::

            >>> expr = [(0, 4), (4, 4), (8, 4), (12, 4), (16, 4)]
            >>> for x in timesignaturetools.fit_meters_to_expr(
            ...     expr, meters):
            ...     print x.implied_time_signature
            ...
            4/4
            4/4
            4/4
            4/4

    ..  container:: example

        **Example 2.** Matching a series of hypothetical 5/4 measures:

        ::

            >>> expr = [(0, 4), (3, 4), (5, 4), (10, 4), (15, 4), (20, 4)]
            >>> for x in timesignaturetools.fit_meters_to_expr(
            ...     expr, meters):
            ...     print x.implied_time_signature
            ...
            5/4
            5/4
            5/4
            5/4

    Offsets are coerced from `expr` via
    `MetricAccentKernel.count_offsets_in_expr()`.

    MetricalHierarchies are coerced from `meters` via
    `MetricalHierarchyInventory`.

    Returns list.
    '''
    from abjad.tools import timesignaturetools

    offset_counter = \
        timesignaturetools.MetricAccentKernel.count_offsets_in_expr(expr)
    ordered_offsets = sorted(offset_counter, reverse=True)
    if not ordered_offsets:
        return []

    if starting_offset is None:
        start_offset = durationtools.Offset(0)
    else:
        start_offset = durationtools.Offset(starting_offset)

    metrical_hierarchy_inventory = datastructuretools.TypedTuple(
        tokens=meters,
        item_class=timesignaturetools.Meter,
        )
    longest_hierarchy = sorted(metrical_hierarchy_inventory,
        key=lambda x: x.preprolated_duration, reverse=True)[0]
    longest_kernel_duration = max(
        x.preprolated_duration for x in metrical_hierarchy_inventory)
    kernels = [x.generate_offset_kernel_to_denominator(denominator)
        for x in metrical_hierarchy_inventory]

    current_start_offset = start_offset
    selected_hierarchies = []

    while len(ordered_offsets) and ordered_offsets[-1] < current_start_offset:
        ordered_offsets.pop()

    while len(ordered_offsets) and current_start_offset <= ordered_offsets[-1]:
        if len(ordered_offsets) == 1:
            if discard_final_orphan_downbeat:
                if ordered_offsets[0] == current_start_offset:
                    break
        current_stop_offset = current_start_offset + longest_kernel_duration
        current_offset_counter = {}
        for offset in reversed(ordered_offsets):
            if current_start_offset <= offset <= current_stop_offset:
                current_offset_counter[offset - current_start_offset] = \
                    offset_counter[offset]
            else:
                break
        if not current_offset_counter:
            winner = longest_hierarchy
        else:
            candidates = []
            for i, kernel in enumerate(kernels):
                response = kernel(current_offset_counter)
                candidates.append((response, i))
            candidates.sort(key=lambda x: x[0], reverse=True)
            response, index = candidates[0]
            winner = metrical_hierarchy_inventory[index]
        selected_hierarchies.append(winner)
        current_start_offset += winner.preprolated_duration
        while len(ordered_offsets) \
            and ordered_offsets[-1] < current_start_offset:
            ordered_offsets.pop()

    return selected_hierarchies