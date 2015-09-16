Feature: Student List
	Scenario Outline: List all students in a section given course number
		Given the input "<code>" "<file>"
		When the program is run
		Then the output should be "<output>"
		Examples:
		| code	   | file													 | output|
		| CORE110.T21 | /home/ubuntu/badStudFinder/CS374_2016_registrations.csv | John Dewing\nNicole Graves\nEvelyn Mcdavid\nKatrina Carlson\nDustin Snyder\nSharon Kegley\nVirgie Webb\nTerry Stephens\nKelly Adams\nHope Killian\nStacy Wright\nCody Ross\nAnthony Collins\nJohn Jackson\nSteve Hernandez\nTerry Marchman\nAntonia Griffin\nDonald Warren\nPenny Chauvin\nErnest Craig\nWilliam Savage\nLucila Shasteen\nCharles Hartman\nAngelina Hong\nCalvin Uresti\nSheldon Snow\nCharles Bienkowski\nMarilyn Towler\nWilliam Nichol\nVera Miller\nKatherine Ahrendt\nDawn Cuellar\nRichard Hale\nJay Harris\nDominga Booth\nWilliam Daniel\nMichael Shook\n|
		| CORE110.HT5 | /home/ubuntu/badStudFinder/CS374_2016_registrations.csv | John Witcher\nGeorgia Gormley\nJane Sartori\nJennifer Limerick\nJamal Hanlon\nYolanda Mcgough\nRaymond Thomas\nJoanne Balado\nEdward Dohse\nSean Hamilton\nLorina Thomas\nPatricia Bales\nPaul Varner\nGeorge Mccormick\nNatalie Rodriguez\nKurt Little\nAvery Boutte\nKaren Mullen\nFrank Roloff\n|
