\context Score = "Grouped Rhythmic Staves Score" <<
	\context TimeSignatureContext = "TimeSignatureContext" {
		{
			\time 2/8
			s1 * 1/4
		}
		{
			\time 3/8
			s1 * 3/8
		}
		{
			\time 4/8
			s1 * 1/2
		}
		{
			\time 5/8
			s1 * 5/8
		}
	}
	\context StaffGroup = "Grouped Rhythmic Staves Staff Group" <<
		\context RhythmicStaff = "Staff 1" {
			\context Voice = "Voice 1" {
				{
					\set stemLeftBeamCount = #0
					\set stemRightBeamCount = #1
					c'8 [
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
				}
				{
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #1
					c'8
					\set stemLeftBeamCount = #1
					\set stemRightBeamCount = #0
					c'8 ]
				}
				{
					s1 * 5/8
				}
			}
		}
	>>
>>