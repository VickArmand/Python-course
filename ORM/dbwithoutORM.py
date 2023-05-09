#!/usr/bin/env python3
# MySQLdb is a connector/driver used in python to connect to mysql database
import MySQLdb as mysql

# Illustrating mysql database connection in python
# .connect(host, user, password, dbname)
db = mysql.connect(host = 'localhost', user = 'root', passwd = '', db = 'blogs')
print(f"Connection created successfully {db}")
# think of a cursor as a database session for interaction
# creating a cursor
cur = db.cursor()
print("Cursor created "+ cur)
# Creating tables using the same created cursor
createquery= "CREATE TABLE IF NOT EXISTS posts (id INT UNSIGNED PRIMARY KEY AUTO_INCREMENT, body TEXT NOT NULL )"
cur.execute(createquery)
# insert query using the same cursor
# for database changes (update and create) we need to commit them after executing
cur.execute("INSERT INTO posts(content) VALUES (%s)",['Hello World'] )
cur.execute("INSERT INTO posts(content) VALUES (%s)",['Second Post'] )
db.commit()
# fetch records 
query = 'SELECT * FROM posts'
num_rows = cur.execute(query)
print('{num_rows} records available')
# fetchall returns all rows fetched
rows = cur.fetchall()
for row in rows:
    print(row)
# just like normal sessions have to be closed simlar to cursors and db connections
cur.close()
db.close()