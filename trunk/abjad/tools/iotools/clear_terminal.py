# -*- encoding: utf-8 -*-
import os


def clear_terminal():
    '''Run ``clear`` if OS is POSIX-compliant (UNIX / Linux / MacOS).

    Run ``cls`` if OS is not POSIX-compliant (Windows):

    ::

        >>> iotools.clear_terminal() # doctest: +SKIP

    Return none.
    '''
    from abjad.tools import iotools

    if os.name == 'posix':
        iotools.spawn_subprocess('clear')
    else:
        iotools.spawn_subprocess('cls')
