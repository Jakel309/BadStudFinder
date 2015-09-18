import sys
import re
import csv
import mysql.connector

db = mysql.connector.connect(user='root', password='password',
	host='127.0.0.1', database='db')
cursor = db.cursor()

query = ""

if re.search('[a-zA-Z]',sys.argv[1]):
	fullCourse=sys.argv[1].translate(None,'[],').split('.')
	secNum=fullCourse[1]
	course=re.match(r"([A-Z]+)([0-9]+)",fullCourse[0],re.I)
	if course:
		items=course.groups()
	query = ''.join(["select `First Name`, `Last Name` from registrations where",
		"`Subject Code` = '", items[0], "' and `Course Number` = ", items[1],
		" and `Section Number` like '%", secNum, "%';"])
	# try:
		# f=open(sys.argv[2].translate(None,'[]'),'rb')
	# except IndexError:
		# f=open("CS374_2016_registrations.csv",'rb')
	# try:
		# reader=csv.DictReader(f)
		# for row in reader:
			# if row['Subject Code']==items[0] and row['Course Number']==items[1] and ((re.search('[a-zA-Z]', row['Section Number']) and re.search('[a-zA-Z]', secNum) and row['Section Number']==secNum) or (not re.search('[a-zA-Z]', row['Section Number']) and not re.search('[a-zA-Z]', secNum) and int(row['Section Number'])==int(secNum))):
				# print row['First Name']+' '+row['Last Name']
	# finally:
		# f.close()
else:
	crn=sys.argv[1].translate(None,'[],')
	query = ''.join(["select `First Name`, `Last Name` from registrations where",
		"CRN = '", crn, "';"])
	# try:
		# f=open(sys.argv[2].translate(None,'[]'),'rb')
	# except IndexError:
		# f=open("CS374_2016_registrations.csv",'rb')
	# try:
		# reader=csv.DictReader(f)
		# for row in reader:
			# if row['CRN']==crn:
				# print row['First Name']+' '+row['Last Name']
	# finally:
		# f.close()

cursor.execute(query)

for (fname, lname) in cursor:
	print fname + ' ' + lname

db.close();