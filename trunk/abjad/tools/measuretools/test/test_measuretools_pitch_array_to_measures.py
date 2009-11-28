from abjad import *


def test_measuretools_pitch_array_to_measure_list_01( ):

   array = pitchtools.PitchArray([
      [1, (2, 1), ([-2, -1.5], 2)],
      [(7, 2), (6, 1), 1],
      ])   

   '''
   [  ] [d'] [bf bqf    ]
   [g'     ] [fs'   ] [ ]
   '''

   measures = measuretools.pitch_array_to_measure_list(array)
   score = Score(Staff([ ]) * 2)
   score[0].append(measures[0])
   score[1].append(measures[1])

   r'''
   \new Score <<
           \new Staff {
                   {
                           \time 4/8
                           r8
                           d'8
                           <bf bqf>4
                   }
           }
           \new Staff {
                   {
                           \time 4/8
                           g'4
                           fs'8
                           r8
                   }
           }
   >>
   '''
   
   assert check.wf(score)
   assert score.format == "\\new Score <<\n\t\\new Staff {\n\t\t{\n\t\t\t\\time 4/8\n\t\t\tr8\n\t\t\td'8\n\t\t\t<bf bqf>4\n\t\t}\n\t}\n\t\\new Staff {\n\t\t{\n\t\t\t\\time 4/8\n\t\t\tg'4\n\t\t\tfs'8\n\t\t\tr8\n\t\t}\n\t}\n>>"
