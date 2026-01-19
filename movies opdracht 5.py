import sqlite3

conn = sqlite3.connect('movies.db')

cursor = conn.cursor()

#cursor.execute('ALTER TABLE movies ADD COLUMN rating REAL')

cursor.execute('''
UPDATE movies
SET rating = 8.0
WHERE title LIKE "Star Wars%"

''')

cursor.execute('''
SELECT id, title, rating FROM movies
WHERE title LIKE "Star Wars%"
''')

for row in cursor:
    print(row)

#hier heb ik gebruik gemaakt van een ICT vriendin + een oude windesheim powerpoint omdat ik bij god niet meer wist hoe alter table zat