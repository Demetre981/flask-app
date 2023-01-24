import sqlite3

connection = sqlite3.connect("app.db")
print("Db created!")

connection.execute("CREATE TABLE article (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, intro TEXT, text TEXT)")
print("Table created")

# cursor = connection.cursor()


# cursor.execute("DELETE FROM article WHERE id=6")


# connection.commit()

connection.close()


