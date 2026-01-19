import sqlite3

conn = sqlite3.connect('movies.db')

cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS directors(
    movie_id INTEGER,
    person_id INTEGER,
    FOREIGN KEY(movie_id) REFERENCES movies(id)
    FOREIGN KEY(person_id) REFERENCES people(id))

''')

george_id = 184
cursor.execute('SELECT id FROM movies WHERE title LIKE "Star Wars:%"')
starwars_movies = cursor.fetchall()

for (movie_id,) in starwars_movies:
    cursor.execute('INSERT OR IGNORE INTO directors(movie_id, person_id) VALUES(?,?)',
                   (movie_id, george_id))

cursor.execute('''
SELECT movies.title, people.name
FROM directors
JOIN people ON directors.person_id = people.id
JOIN movies ON directors.movie_id = movies.id
WHERE people.id = 184
''')

for row in cursor:
    print(row)