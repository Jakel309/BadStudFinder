import mysql.connector
import random;

db = mysql.connector.connect(user='root', password='password',
	host='127.0.0.1', database='db')
cursor = db.cursor()

cursor.execute("update enrollment set Semester = 3, Year = 2015")

cursor.execute("select `Banner ID` from student")

grades = ['A', 'B', 'C', 'D', 'F', 'W']

banners = []

for (banner) in cursor:
	banners.append(banner)
for (banner) in banners:
	for i in range(0, random.randint(15, 25)):
		course = random.randint(1, 11573)
		grade = grades[random.randint(0, 5)]
		sem = random.randint(1, 3)
		year = random.randint(2010, 2015)
		if (year == 2015 and sem == 3):
			sem = 2
		cursor.execute(''.join(["insert into enrollment values(", str(banner), ",",
			str(course), ",", str(sem), ",", str(year), ",'", str(grade), "');"]))