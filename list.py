import sys
import re
import mysql.connector
import string
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("config.ini")
Config.sections()
def ConfigSectionMap(section):
    dict1 = {}
    options = Config.options(section)
    for option in options:
        try:
            dict1[option] = Config.get(section, option)
            if dict1[option] == -1:
                DebugPrint("skip: %s" % option)
        except:
            print("exception on %s!" % option)
            dict1[option] = None
    return dict1

db = mysql.connector.connect(user=ConfigSectionMap("Database")['user'], password=ConfigSectionMap("Database")['password'],
	host=ConfigSectionMap("Database")['host'], database=ConfigSectionMap("Database")['database'])
cursor = db.cursor()

crn = ""
cursor.execute(''.join(["select max(`Term Code`) from enrollment"]))
termCode=cursor.fetchone()[0]
f=open('prereqs.txt','r')

part=1

course=''
prereqs=[]
classification=''
for line in f:
	if list(line)[0]+list(line)[1]!='--':
		if part==1:
			course=line.replace("\n","").replace("\r","")
			course=re.match(r"([a-z]+)([0-9]+)", course, re.I)
			if course:
				course=course.groups()
			if type(course[1]) is str:
				course=(course[0],int(course[1]))
			part=part+1
		elif part==2:
			stuff=line.split(',')
			for i in stuff:
				prereqs.append(i.replace("\n","").replace("\r",""))
			part=part+1
		elif part==3:
			classification=line.replace("\n","").replace("\r","")
			part=1

			cursor.execute(''.join(["select st.`Banner ID`, st.`First Name`, st.`Last Name`, se.`Section Number` from",
				" section se inner join enrollment e on e.CRN = se.CRN inner join",
				" student st on e.`Banner ID` = st.`Banner ID` where",
				" se.`Subject Code`='",course[0],"' and se.`Course Number`=",str(course[1])," and se.`Term Code`=",str(termCode)," order by se.`Section Number`;"]))

			students={}
			section={}

			for (banner, fName, lName, sNum) in cursor:
				name=fName+' '+lName
				students[name]=banner
				section[name]=sNum

			for stud in students:
				index=0
				for i in prereqs:
					orPrereqs=i.split('*')
					notPassed=True
					orFailPre=[]
					for prereq in orPrereqs:
						prereq=prereq.split(':')
						sub=re.match(r"([a-z]+)([0-9]+)", prereq[0], re.I)
						if sub:
							sub=sub.groups()
						if type(sub[1]) is str:
							sub=(sub[0],int(sub[1]))
						cursor.execute(''.join(["select e.Grade from ",
							"section s inner join enrollment e on e.CRN=s.CRN where ",
							"e.`Banner ID` = '",str(students[stud]),"' and s.`Subject Code` = '",sub[0],"' and s.`Course Number` = ",str(sub[1])," and e.`Term Code` = "
							"(select max(e.`Term Code`) from section s inner join enrollment e on e.CRN = s.CRN ",
							"where e.`Banner ID` = '",str(students[stud]),"' and s.`Subject Code` = '",sub[0],"' and s.`Course Number` = ",str(sub[1])," and e.`Term Code`<>",str(termCode),");"]))
						try:
							grade=cursor.fetchone()[0]
							if grade>prereq[1]:
								orFailPre.append(prereq)
							else:
								notPassed=False
						except:
							orFailPre.append(prereq)
					if notPassed:
						for prereq in orPrereqs:
							prereq=prereq.split(':')
							sub=re.match(r"([a-z]+)([0-9]+)", prereq[0], re.I)
							if sub:
								sub=sub.groups()
							if type(sub[1]) is str:
								sub=(sub[0],int(sub[1]))
							cursor.execute(''.join(["select e.Grade from ",
								"section s inner join enrollment e on e.CRN=s.CRN where ",
								"e.`Banner ID` = '",str(students[stud]),"' and s.`Subject Code` = '",sub[0],"' and s.`Course Number` = ",str(sub[1])," and e.`Term Code` = "
								"(select max(e.`Term Code`) from section s inner join enrollment e on e.CRN = s.CRN ",
								"where e.`Banner ID` = '",str(students[stud]),"' and s.`Subject Code` = '",sub[0],"' and s.`Course Number` = ",str(sub[1])," and e.`Term Code`<>",str(termCode),");"]))
							try:
								grade=cursor.fetchone()[0]
								if grade>prereq[1]:
									print stud+" "+students[stud]+" recieved a "+grade+" in "+prereq[0]+" expected "+prereq[1]+" for course: "+course[0]+str(course[1])+"."+section[stud]
								else:
									notPassed=False
							except:
								print stud+" "+students[stud]+" did not complete "+prereq[0]+" for course: "+course[0]+str(course[1])+"."+section[stud]
			course=''
			prereqs=[]
			classification=''

db.close();
