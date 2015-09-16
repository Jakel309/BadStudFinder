import sys
import re
import csv

if re.search('[a-zA-Z]',sys.argv[1]):
	fullCourse=sys.argv[1].translate(None,'[],').split('.')
	secNum=fullCourse[1]
	course=re.match(r"([A-Z]+)([0-9]+)",fullCourse[0],re.I)
	if course:
		items=course.groups()
	try:
		f=open(sys.argv[2].translate(None,'[]'),'rb')
	except IndexError:
		f=open("CS374_2016_registrations.csv",'rb')
	try:
		reader=csv.DictReader(f)
		for row in reader:
			if row['Subject Code']==items[0] and row['Course Number']==items[1] and ((re.search('[a-zA-Z]', row['Section Number']) and re.search('[a-zA-Z]', secNum) and row['Section Number']==secNum) or (not re.search('[a-zA-Z]', row['Section Number']) and not re.search('[a-zA-Z]', secNum) and int(row['Section Number'])==int(secNum))):
				print row['First Name']+' '+row['Last Name']
	finally:
		f.close()
else:
	crn=sys.argv[1].translate(None,'[],')
	try:
		f=open(sys.argv[2].translate(None,'[]'),'rb')
	except IndexError:
		f=open("CS374_2016_registrations.csv",'rb')
	try:
		reader=csv.DictReader(f)
		for row in reader:
			if row['CRN']==crn:
				print row['First Name']+' '+row['Last Name']
	finally:
		f.close()