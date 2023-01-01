import sqlite3

# Connect to DB and Create a Cursor
sqliteConnection = sqlite3.connect ('sql.db')
cursor=sqliteConnection.cursor()
print('DB Init')

#Write a Query and Execute it With cursor
query='select sqlite_version()'
cursor.execute(query)

#Fetch and Output Result
result=cursor.fetchall()
print('SQLite Version is ()'.format(result))

#close the cursor
cursor.close()

#close DB connection
sqliteConnection.close()
print('SQLite connection closed')
