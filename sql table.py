import sqlite3
conn=sqlite3.connect('are.db')
cursor=conn.cursor()
cursor.execute('''drop table if exists student''')
table="""CREATE TABLE STUDENT (NAME text,CLASS text,SELECTION text);"""
cursor.execute(table)
cursor.execute('''INSERT INTO STUDENT VALUES ('Raju','7th','A')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Shyam','8th','B')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Baburao','9th','C')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Ajay','4th','C')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Rahul','5th','C')''')
cursor.execute('''INSERT INTO STUDENT VALUES ('Shiv','6th','C')''')

print("Data Inserted in the table:")
cursor.execute("DELETE FROM STUDENT WHERE class='5th'")
for row in data:
      print(row)
conn.commit()
conn.close()
       
