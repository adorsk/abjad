# -*- encoding: utf-8 -*-


def negate_absolute_value_of_sequence_elements_at_indices(sequence, indices):
    '''Negate the absolute value of `sequence` elements at `indices`:

    ::

        >>> sequence = [1, 2, 3, 4, 5, -6, -7, -8, -9, -10]

    ::

        >>> sequencetools.negate_sequence_elements_at_indices(sequence, [0, 1, 2])
        [-1, -2, -3, 4, 5, -6, -7, -8, -9, -10]

    Returns newly constructed list.
    '''

    result = []

    for i, element in enumerate(sequence):
        if (i in indices):
            result.append(-abs(element))
        else:
            result.append(element)

    return result
