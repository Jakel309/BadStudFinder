Feature: Student List
	Scenario Outline: List all students in course given a crn
		Given the input "<code>"
		When the program is run with no file
		Then the output now should be "<output>"
		Examples:
		| code	   | output|
		| 10263	   | Donnie Ross\nDennis Pare\nMichele Chapin\nJudy Addison\nRichard Smith\nHenry Franks\nWilliam Yardley\nPatricia Weeden\nKenny Nolte\nChristoper Martin\nDonald Barmore\nJohn Lozon\n|
