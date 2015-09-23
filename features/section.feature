Feature: Student List
	Scenario Outline: List all students in a section given course number
		Given the input "<code>"
		When the program is run
		Then the output should be "<output>"
		Examples:
		| code	   | output|
		| CORE110.T21 | Kelly Adams, 000997288\nKatherine Ahrendt, 000078556\nCharles Bienkowski, 000543398\nDominga Booth, 000076941\nKatrina Carlson, 000393670\nPenny Chauvin, 000337634\nAnthony Collins, 000335085\nErnest Craig, 000458641\nDawn Cuellar, 000886014\nWilliam Daniel, 000586136\nJohn Dewing, 000868168\nNicole Graves, 000001339\nAntonia Griffin, 000284147\nRichard Hale, 000760052\nJay Harris, 000823049\nCharles Hartman, 000058767\nSteve Hernandez, 000194167\nAngelina Hong, 000983768\nJohn Jackson, 000640979\nSharon Kegley, 000506075\nHope Killian, 000863460\nTerry Marchman, 000041934\nEvelyn Mcdavid, 000903983\nVera Miller, 000229433\nWilliam Nichol, 000450556\nCody Ross, 000336809\nWilliam Savage, 000288218\nLucila Shasteen, 000167212\nMichael Shook, 000322296\nSheldon Snow, 000733120\nDustin Snyder, 000901420\nTerry Stephens, 000662800\nMarilyn Towler, 000865951\nCalvin Uresti, 000554968\nDonald Warren, 000383410\nVirgie Webb, 000149227\nStacy Wright, 000027722\n|
		| CORE110.HT5 | Joanne Balado, 000166401\nPatricia Bales, 000152998\nAvery Boutte, 000397364\nEdward Dohse, 000531670\nGeorgia Gormley, 000456457\nSean Hamilton, 000146153\nJamal Hanlon, 000207521\nJennifer Limerick, 000857217\nKurt Little, 000749916\nGeorge Mccormick, 000945598\nYolanda Mcgough, 000287022\nKaren Mullen, 000775583\nNatalie Rodriguez, 000034663\nFrank Roloff, 000637358\nJane Sartori, 000271317\nLorina Thomas, 000661741\nRaymond Thomas, 000181832\nPaul Varner, 000704276\nJohn Witcher, 000587153\n|
