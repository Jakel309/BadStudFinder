import sys
import re
import mysql.connector
import string

#data entered in this order "'Course' 'Comma deliminated requirements'"

db = mysql.connector.connect(user='root', password='password',
	host='127.0.0.1', database='db')
cursor = db.cursor()

def is_ascii(s):
    try:
        s.decode('ascii')
        return True
    except UnicodeDecodeError:
        return False

crn = ""
cursor.execute(''.join(["select max(`Term Code`) from enrollment"]))
termCode=cursor.fetchone()[0]
f=open('prereqs.txt','r')

part=1

course=''
prereqs={}
prereqsOld=[]
classification=''
crn = ""
for line in f:
	if list(line)[0]+list(line)[1]!='--':
		if part==1:
			course=line.replace("\n","").replace("\r","")
			part=part+1
		elif part==2:
			stuff=line.split(',')
			for i in stuff:
				stuff2=i.split(':')
				prereqsOld.append(stuff2[0])
				if re.search('[a-zA-Z]', stuff2[0]):
					fullCourse = stuff2[0].translate(None, '[],').split('.')
					secNum = fullCourse[1]
					stuff2[0] = re.match(r"([A-Z]+)([0-9]+)", fullCourse[0], re.I)
					if stuff2[0]:
						items = stuff2[0].groups()
					cursor.execute(''.join(["select `CRN` from ",
						"section where `Subject Code` = '", items[0], 
						"' and `Course Number` = ", items[1], " and `Section Number` like '%", 
						secNum, "';"]))
					stuff2[0] = cursor.fetchone()[0];
				prereqs[stuff2[0]]=stuff2[1].replace("\n","").replace("\r","")
			part=part+1
		elif part==3:
			classification=line.replace("\n","").replace("\r","")
			print course
			print prereqs
			print classification
			part=1

			if re.search('[a-zA-Z]', course):
				fullCourse = course.translate(None, '[],').split('.')
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
				crn = course.translate(None,'[],')

			cursor.execute(''.join(["select s.`Banner ID`, s.`First Name`, s.`Last Name` from ",
				"enrollment e inner join student s on e.`Banner Id` = s.`Banner ID` where ",
				"CRN = '", str(crn), "' and e.`Term Code`='",str(termCode),"' order by `Last Name`;"]))

			students={}

			for (banner, fName, lName) in cursor:
				name=fName+' '+lName
				students[name]=banner

			for stud in students:
				index=0
				for prereq in prereqs:
					cursor.execute(''.join(["select Grade from ",
						"enrollment where `Banner ID`='",str(students[stud]),"' and ",
						"CRN='",str(prereq),"' and `Term Code`=",
						"(select max(`Term Code`) from enrollment where ",
						"`Banner ID`='",str(students[stud]),"' and CRN='",str(prereq),"');"]))
					try:
						grade=cursor.fetchone()[0]
						if grade>prereqs[prereq]:
							print stud+" "+students[stud]+" recieved a "+grade+" in "+prereqsOld[index]+" expected "+prereqs[prereq]
							break
					except:
						print stud+" "+students[stud]+" did not complete "+prereqsOld[index]
						break
					index=index+1

db.close();