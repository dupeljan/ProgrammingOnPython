import os
import sqlite3
import html

from lxml import etree
from lxml import builder

types = ["INTEGER","TEXT","DATE"]	

def createTables(db,cursor):
	cursor.execute("CREATE TABLE genre(id " + types[0] + " PRIMARY KEY, name " + types[1] + ")")
	cursor.execute("CREATE TABLE musician(id " + types[0] + " PRIMARY KEY, name " + types[1] + ", DOB " + types[2] + ")")
	cursor.execute("CREATE TABLE music(id " + types[0] + " PRIMARY KEY, name " + types[1] + ", musician_id " + types[0] + " REFERENCES musician(id), genre_id " + types[0] + " REFERENCES genre(id))")
	db.commit()

def createData(db,cursor):	
	cursor.execute("INSERT INTO genre VALUES(?,?)",(0,"Classic music"))
	cursor.execute("INSERT INTO genre VALUES(?,?)",(1,"Pop music"))
	cursor.execute("INSERT INTO genre VALUES(?,?)",(2,"Hip-Hop music"))
	cursor.execute("INSERT INTO musician VALUES(?,?,?)",(0,"Иоганн Себастьян Бах","1685-03-31"))
	cursor.execute("INSERT INTO musician VALUES(?,?,?)",(1,"Вольфган Амадей Моцарт","1756-01-27"))
	cursor.execute("INSERT INTO music VALUES(?,?,?,?)",(0,"Цвет настроения синий",1,2))
	cursor.execute("INSERT INTO music VALUES(?,?,?,?)",(1,"Беливер",0,0))
	db.commit()

def Query1(cursor, query, root = None, toXML = False):
	print("query1")
	cursor.execute(query)
	while True:
		row = cursor.fetchone()
		if not row: break
		id,name = row
		if toXML:
			record = etree.SubElement(root,"genre")
			etree.SubElement(record, "id").text = str(id) + "," + types[0]
			etree.SubElement(record, "name").text = name + "," + types[1]
		else:
			print(id,name)
	if toXML:
		return root

def Query2(cursor, query, root = None, toXML = False):
	print("query2")
	cursor.execute(query)
	while True:
		row = cursor.fetchone()
		if not row: break
		id,name,DOB = row
		if toXML:
			record = etree.SubElement(root,"musician")
			etree.SubElement(record, "id").text = str(id) + "," + types[0]
			etree.SubElement(record, "name").text = name + "," + types[1]
			etree.SubElement(record, "DOB").text = str(DOB) + "," + types[2]
		else:
			print(id,name,DOB)
	if toXML:
		return root

def Query3(cursor, query, root = None, toXML = False):
	print("query3")
	cursor.execute(query)
	while True:
		row = cursor.fetchone()
		if not row: break
		id,name,name2,DOB,name3 = row
		if toXML:
			record = etree.SubElement(root,"allTables")
			etree.SubElement(record, "id").text = str(id) + "," + types[0]
			etree.SubElement(record, "name_misic").text = name + "," + types[1]
			etree.SubElement(record, "name_musician").text = name2 + "," + types[1]
			etree.SubElement(record, "DOB_musician").text = str(DOB) + "," + types[2]
			etree.SubElement(record, "name_genre").text = name3 + "," + types[1]
		else:
			print(id,name,name2,DOB,name3)
	if toXML:
		return root
	
def fromDBToXML(root):
	resStrXML = etree.tostring(root,encoding='utf-8',pretty_print=True).decode('utf-8')
	print(resStrXML)
	resXMLFile = open("resXMLFile.xml","w")
	resXMLFile.write(resStrXML)

def fromXMLToDB():
	dbFileName = "ResGenreMusic.db"
	conn = sqlite3.connect(dbFileName)
	cursor = conn.cursor()
	tables = []
	fobj = open("resXMLFile.xml")
	xml = fobj.read()
	root = etree.fromstring(xml)
	for appt in root.getchildren():
		if appt.tag not in tables:
			query = "CREATE TABLE " + appt.tag + "("
			for elem in appt.getchildren():
				query += elem.tag + " " + elem.text.split(',')[1] + ","
			query = query[:-1] + ")"
			cursor.execute(query)
			conn.commit()
			tables.append(appt.tag)
		query = "INSERT INTO " + appt.tag + " VALUES ("
		for elem in appt.getchildren():
			value,type = elem.text.split(',')
			if type == types[0]:
				query += value + ","
			else:
				query += "\"" + value + "\" ,"
		query = query[:-1] + ")"
		print(query)
		cursor.execute(query)
		conn.commit()


dbFileName = "GenreMusic.db"
create = not os.path.exists(dbFileName)
conn = sqlite3.connect(dbFileName)
if create:
	cursor = conn.cursor()
	createTables(conn,cursor)
	createData(conn,cursor)

cursor2 = conn.cursor()
root = etree.Element("root")
root = Query1(cursor2,"SELECT * FROM genre where name LIKE \'C%\'",root,True)
root = Query2(cursor2,"SELECT * FROM musician where DOB < \'1700-01-02\'",root,True)
root = Query3(cursor2,"SELECT m.id,m.name,mu.name,mu.DOB,g.name FROM music m JOIN musician mu ON(m.musician_id = mu.id) JOIN genre g ON(m.genre_id=g.id)",root,True)
fromDBToXML(root)
fromXMLToDB()
conn = sqlite3.connect("Res" + dbFileName)
cursor2 = conn.cursor()
Query1(cursor2,"SELECT * FROM genre",False)
Query2(cursor2,"SELECT * FROM musician",False)
Query3(cursor2,"SELECT * FROM allTables",False)
