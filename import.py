import mysql.connector
from glob import glob

db = mysql.connector.connect(user='root', password='password',
	host='127.0.0.1', database='db', allow_local_infile=True)
cursor = db.cursor()

#create (replace) registration table
for line in open("registrations.sql").read().split(';\n'):
    cursor.execute(line)

#get all csv files
for path in glob("csvs/*.csv"):
	#import each file
	cursor.execute("".join(["load data local infile '", path , "' ",
		"into table db.registrations ",
		"fields terminated by ',' enclosed by '\"' ",
		"lines terminated by '\n'; "]))
#clean up empty rows
cursor.execute("delete from registrations where crn = 0;")

#dump into real tables, then it's ready to go
for line in open("tables.sql").read().split(';\n'):
    cursor.execute(line)