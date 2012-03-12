from abjad import *
import py.test


def testContextMark___setattr___01():
    '''Slots constraint context mark attributes.
    '''

    context_mark = contexttools.ContextMark()

    assert py.test.raises(AttributeError, "context_mark.foo = 'bar'")
