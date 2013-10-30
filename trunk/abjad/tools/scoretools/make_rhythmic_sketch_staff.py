# -*- encoding: utf-8 -*-


def make_rhythmic_sketch_staff(music):
    r'''Make rhythmic staff with transparent time_signature and transparent bar
    lines.
    '''
    from abjad.tools import scoretools

    staff = scoretools.Staff(music)
    staff.context_name = 'RhythmicStaff'
    staff.override.time_signature.transparent = True
    staff.override.bar_line.transparent = True

    return staff