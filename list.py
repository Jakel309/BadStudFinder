import sys
import re
import mysql.connector

db = mysql.connector.connect(user='root', password='password',
	host='127.0.0.1', database='db')
cursor = db.cursor()

crn = ""

if re.search('[a-zA-Z]', sys.argv[1]):
	fullCourse = sys.argv[1].translate(None, '[],').split('.')
	secNum = fullCourse[1]
	course = re.match(r"([A-Z]+)([0-9]+)", fullCourse[0], re.I)
	if course:
		items = course.groups()
	cursor.execute(''.join(["select `CRN` from ",
		"section where `Subject Code` = '", items[0], 
		"' and `Course Number` = ", items[1], " and `Section Number` like '%", 
		secNum, "';"]))
	crn = cursor.fetchone()[0];
else:
	crn = sys.argv[1].translate(None,'[],')

cursor.execute(''.join(["select s.`First Name`, s.`Last Name`, s.`Banner ID` from",
	" enrollment e inner join student s on e.`Banner Id` = s.`Banner ID` where ",
	"CRN = '", str(crn), "';"]))

for (fname, lname, banner) in cursor:
	print fname + ' ' + lname + ', ' + banner

db.close();