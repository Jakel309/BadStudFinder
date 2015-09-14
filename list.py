import sys
import re
import csv

fullCourse=sys.argv[1].translate(None,'[]').split('.')
secNum=fullCourse[1]
course=re.match(r"([A-Z]+)([0-9]+)",fullCourse[0],re.I)
if course:
	items=course.groups()
f=open(sys.argv[2].translate(None,'[]'),'rb')
try:
	reader=csv.DictReader(f)
	for row in reader:
		if row['Subject Code']==items[0] and row['Course Number']==items[1] and int(row['Section Number'])==int(secNum):
			print row['First Name']+' '+row['Last Name']
finally:
	f.close()
