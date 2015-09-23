import mysql.connector
import random;

db = mysql.connector.connect(user='root', password='password',
	host='127.0.0.1', database='db')
cursor = db.cursor()

cursor.execute("select `Banner ID` from student;")

grades = ['A', 'B', 'C', 'D', 'F', 'W']

banners = []

for (banner) in cursor:
	banners.append(banner)
for (banner) in banners:
	for i in range(0, random.randint(15, 25)):
		course = random.randint(1, 11573)
		grade = grades[random.randint(0, 5)]
		sem = random.randint(1, 3)
		year = random.randint(2005, 2015)
		cursor.execute(''.join(["insert into enrollment values(", banner[0], ",",
			str(course), ",", str(year), str(sem), "0,'", str(grade), "') ON DUPLICATE KEY UPDATE CRN = CRN;"]))

db.commit()
