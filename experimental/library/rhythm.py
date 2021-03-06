from abjad import *
__all__ = []


dotted_eighths = rhythmmakertools.TaleaRhythmMaker(
    talea=(3, 1), 
    talea_denominator=16, 
    beam_cells_together=True,
    )
dotted_eighths.name = 'dotted_eighths'
__all__.append(dotted_eighths.name)


dotted_sixteenths = rhythmmakertools.TaleaRhythmMaker(
    talea=(3, 1), 
    talea_denominator=32, 
    beam_cells_together=True,
    )
dotted_sixteenths.name = 'dotted_sixteenths'
__all__.append(dotted_sixteenths.name)


dotted_thirty_seconds = rhythmmakertools.TaleaRhythmMaker(
    talea=(3, 1), 
    talea_denominator=64, 
    beam_cells_together=True,
    )
dotted_thirty_seconds.name = 'dotted_thirty_seconds'
__all__.append(dotted_thirty_seconds.name)


eighths = rhythmmakertools.TaleaRhythmMaker(
    talea=(1,), 
    talea_denominator=8, 
    beam_cells_together=True,
    )
eighths.name = 'eighths'
__all__.append(eighths.name)


# this isn't the best pattern because initialization of the rhythm-maker 
# resets beam_cells_together
equal_divisions = rhythmmakertools.EqualDivisionRhythmMaker
equal_divisions.beam_each_cell = True
equal_divisions.name = 'equal_divisions'
__all__.append(equal_divisions.name)


even_runs = rhythmmakertools.EvenRunRhythmMaker
even_runs.beam_each_cell = True
even_runs.name = 'even_runs'
__all__.append(even_runs.name)


halves = rhythmmakertools.TaleaRhythmMaker(
    talea=(1,), 
    talea_denominator=2, 
    beam_cells_together=False,
    )
halves.name = 'halves'
__all__.append(halves.name)


note_tokens = rhythmmakertools.NoteRhythmMaker(
    beam_cells_together=False,
    beam_each_cell=False,
    )
note_tokens.name = 'note_tokens'
__all__.append(note_tokens.name)


quarters = rhythmmakertools.TaleaRhythmMaker(
    talea=(1,), 
    talea_denominator=4, 
    beam_cells_together=False,
    )
quarters.name = 'quarters'
__all__.append(quarters.name)


rest_tokens = rhythmmakertools.RestRhythmMaker()
rest_tokens.name = 'rest_tokens'
__all__.append(rest_tokens.name)


sixteenths = rhythmmakertools.TaleaRhythmMaker(
    talea=(1,), 
    talea_denominator=16, 
    beam_cells_together=True,
    )
sixteenths.name = 'sixteenths'
__all__.append(sixteenths.name)


sixty_fourths = rhythmmakertools.TaleaRhythmMaker(
    talea=(1,), 
    talea_denominator=64, 
    beam_cells_together=True,
    )
sixty_fourths.name = 'sixty_fourths'
__all__.append(sixty_fourths.name)


skip_tokens = rhythmmakertools.SkipRhythmMaker()
skip_tokens.name = 'skip_tokens'
__all__.append(skip_tokens.name)


thirty_seconds = rhythmmakertools.TaleaRhythmMaker(
    talea=(1,), 
    talea_denominator=32,
    beam_cells_together=True,
    )
thirty_seconds.name = 'thirty_seconds'
__all__.append(thirty_seconds.name)


tuplet_monads = rhythmmakertools.TupletMonadRhythmMaker()
tuplet_monads.name = 'tuplet_monads'
__all__.append(tuplet_monads.name)
