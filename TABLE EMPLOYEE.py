import sqlite3
conn=sqlite3.connect('are.db')
cursor=conn.cursor()
cursor.execute('''drop table if exists Employee''')
table="""CREATE TABLE EMPLOYEE (NAME text,DEPARTMENT text,SALLARY NUMBER);"""
cursor.execute(table)
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Raju','MANAGEMENT',120000)''')
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Shyam','HR',20000)''')
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Baburao','TESTING',30000)''')
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Ajay','MAINTENANCE',50000)''')
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Rahul','AUTOMATION',80000)''')
cursor.execute('''INSERT INTO EMPLOYEE VALUES ('Shiv','SOFTWARE',85000)''')

print("Data Inserted in the table:")

print("EMPLOYEE Table:")
data = cursor.execute ('''SELECT * FROM EMPLOYEE''')

cursor.execute('''UPDATE EMPLOYEE SALARY  = 2000 WHERE Age<35;''')
print('\n After Updating ...\n')

for row in data:
      print(row)
conn.commit()
conn.close()
