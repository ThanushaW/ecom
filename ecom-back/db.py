import sqlite3

conn = sqlite3.connect("books.sqlite")

# cursor executes sql expression
cursor = conn.cursor()

# sql_query = """CREATE TABLE book(
#     id integer PRIMARY KEY,
#     author text NOT NULL,
#     langauge text NOT NULL,
#     title text NOT NULL
# )"""

# cursor.execute(sql_query)

# sql = "INSERT INTO book (author,langauge,title) VALUES (?,?,?)"
# result = cursor.execute(sql,("thanusha","sinhala","wanaraya"))