Feature: Student List
	Scenario Outline: List all students in course given a course number
		Given the input "<code>" "<file>"
		When the program is run
		Then the output should be "<output>"
		Examples:
		| code	   | file													 | output|
		| ART213.1 | /home/ubuntu/badStudFinder/CS374_2016_registrations.csv | Donnie Ross\nDennis Pare\nMichele Chapin\nJudy Addison\nRichard Smith\nHenry Franks\nWilliam Yardley\nPatricia Weeden\nKenny Nolte\nChristoper Martin\nDonald Barmore\nJohn Lozon\n|
		| ART213.01 | /home/ubuntu/badStudFinder/CS374_2016_registrations.csv | Donnie Ross\nDennis Pare\nMichele Chapin\nJudy Addison\nRichard Smith\nHenry Franks\nWilliam Yardley\nPatricia Weeden\nKenny Nolte\nChristoper Martin\nDonald Barmore\nJohn Lozon\n|
		| ANSC360.L3 | /home/ubuntu/badStudFinder/CS374_2016_registrations.csv | Myra Hook\nJerry Bell\nCaroline Barrett\nMartha Davis\nDaniel James\n|
