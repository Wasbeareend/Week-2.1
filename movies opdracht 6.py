import sqlite3

conn = sqlite3.connect('movies.db')

cursor = conn.cursor()

cursor.execute('''
UPDATE movies
SET rating = 10.0
WHERE title = "Star Wars: Episode VI - Return of the Jedi"
''')

cursor.execute('''
SELECT title, rating
FROM movies
WHERE title = "Star Wars: Episode VI - Return of the Jedi"
''')

for row in cursor:
    print(row)