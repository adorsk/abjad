# -*- encoding: utf-8 -*-
from abjad.tools import topleveltools
from abjad.tools.abctools import AbjadObject


class MaterialManager(AbjadObject):
    r'''Material manager.
    '''

    ### INITIALIZER ###

    def __init__(self):
        pass

    ### PUBLIC METHODS ###

    def register_material(self, material):
        r'''Register `material`.

        Change tuple or list to payload expression.

        Change parseable string to start-positioned rhythm payload expression.
        '''
        from experimental.tools import musicexpressiontools
        if isinstance(material, (tuple, list)):
            return musicexpressiontools.IterablePayloadExpression(material)
        elif isinstance(material, (str)):
            component = topleveltools.parse(material)
            return musicexpressiontools.StartPositionedRhythmPayloadExpression(
                [component], start_offset=0)
        else:
            raise TypeError(material)
