#!/usr/bin/python3
import cgi
import html
import os
import sqlite3

def outputInfo(text):
	print("Content-type: text/html\n")
	print("""<!DOCTYPE HTML>
	        <html>
	        <head>
	            <meta charset="utf-8">
	            <title>Обработка данных форм</title>
	        </head>
	        <body>""")

	print("<h1>Обработка данных форм!</h1>")
	# print("<p>Id: {}</p>".format(text1))
	# print("<p>NAME: {}</p>".format(text2))
	print("<p>text: {}</p>".format(text))

	print("""</body>
	        </html>""")


def createTables(db,cursor):
	types = ["INTEGER","TEXT","DATE"]
	cursor.execute("CREATE TABLE genre(id " + types[0] + " PRIMARY KEY, name " + types[1] + ")")
	cursor.execute("CREATE TABLE musician(id " + types[0] + " PRIMARY KEY, name " + types[1] + ", DOB " + types[2] + ")")
	cursor.execute("CREATE TABLE music(id " + types[0] + " PRIMARY KEY, name " + types[1] + ", musician_id " + types[0] + " REFERENCES musician(id), genre_id " + types[0] + " REFERENCES genre(id))")
	db.commit()

form = cgi.FieldStorage();

dbFileName = "GenreMusic.db"
create = not os.path.exists(dbFileName)
conn = sqlite3.connect(dbFileName)
if create:
	cursor = conn.cursor()
	createTables(conn,cursor)

cursor2 = conn.cursor()

text1 = form.getfirst("IdGenre","не задано")
text2 = form.getfirst("NameGenre","не задано")

cursor2.execute("INSERT INTO genre VALUES(" + text1 + ",\'" + text2 + "\')")
conn.commit()
outputInfo("Yes")