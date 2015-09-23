Feature: Student List
	Scenario Outline: List all students in course given a course number
		Given the input "<code>"
		When the program is run
		Then the output should be "<output>"
		Examples:
		| code	   | output|
		| ART213.1 | Judy Addison, 000360801\nDonald Barmore, 000881951\nMichele Chapin, 000031624\nHenry Franks, 000742767\nJohn Lozon, 000165817\nChristoper Martin, 000470296\nKenny Nolte, 000373791\nDennis Pare, 000191822\nDonnie Ross, 000885148\nRichard Smith, 000970118\nPatricia Weeden, 000083204\nWilliam Yardley, 000672857\n|
		| ART213.01 | Judy Addison, 000360801\nDonald Barmore, 000881951\nMichele Chapin, 000031624\nHenry Franks, 000742767\nJohn Lozon, 000165817\nChristoper Martin, 000470296\nKenny Nolte, 000373791\nDennis Pare, 000191822\nDonnie Ross, 000885148\nRichard Smith, 000970118\nPatricia Weeden, 000083204\nWilliam Yardley, 000672857\n|
		| ANSC360.L3 | Caroline Barrett, 000978232\nJerry Bell, 000240294\nMartha Davis, 000445127\nMyra Hook, 000993095\nDaniel James, 000878236\n|
