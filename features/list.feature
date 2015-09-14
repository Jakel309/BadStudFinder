Feature: Student List
	Scenario: List all students in course
		Given the input 'ART213.1' '/home/ubuntu/badStudFinder/CS374_2016_registrations.csv'
		When the program is run
		Then the output should be "John\nJacob\nJames"
