# -*- encoding: utf-8 -*-
from abjad.tools.sequencetools.is_permutation import is_permutation
import copy


def permute_sequence(sequence, permutation):
    '''Permute `sequence` by `permutation`:

    ::

        >>> sequencetools.permute_sequence([10, 11, 12, 13, 14, 15], [5, 4, 0, 1, 2, 3])
        [15, 14, 10, 11, 12, 13]

    Returns newly constructed `sequence` object.
    '''

    if not is_permutation(permutation, length=len(sequence)):
        args = (str(permutation), len(sequence))
        raise TypeError('"%s" must be permutation of length %s.' % args)

    result = []
    for index in permutation:
        new_element = copy.copy(sequence[index])
        result.append(new_element)
    if isinstance(sequence, str):
        return ''.join(result)
    else:
        return type(sequence)(result)