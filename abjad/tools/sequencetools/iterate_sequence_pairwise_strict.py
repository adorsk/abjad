# -*- encoding: utf-8 -*-


def iterate_sequence_pairwise_strict(sequence):
    '''Iterate `sequence` pairwise strict:

    ::

        >>> list(sequencetools.iterate_sequence_pairwise_strict(range(6)))
        [(0, 1), (1, 2), (2, 3), (3, 4), (4, 5)]

    Returns pair generator.
    '''

    prev = None
    for x in sequence:
        cur = x
        if prev is not None:
            yield prev, cur
        prev = cur