import sqlite3

conn = sqlite3.connect('movies.db')

cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS starwarskoppeling (
    movie_id INTEGER,
    person_id INTEGER,
    FOREIGN KEY (movie_id) REFERENCES movies(id),
    FOREIGN KEY (person_id) REFERENCES people(id))

''')

cursor.execute("INSERT OR IGNORE INTO starwarskoppeling(movie_id, person_id) VALUES(121766, 191)")
cursor.execute("INSERT OR IGNORE INTO starwarskoppeling(movie_id, person_id) VALUES(121766, 204)")
cursor.execute("INSERT OR IGNORE INTO starwarskoppeling(movie_id, person_id) VALUES(121766, 159789)")

cursor.execute('''
SELECT people.name, people.birth
FROM starwarskoppeling
JOIN people ON starwarskoppeling.person_id = people.id
JOIN movies ON starwarskoppeling.movie_id = movies.id
WHERE movies.title = "Star Wars: Episode III - Revenge of the Sith"
''')

for row in cursor:
    print(row)

#https://stackoverflow.com/questions/29420910/how-do-i-enforce-foreign-keys
