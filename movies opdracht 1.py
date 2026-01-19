import sqlite3

conn = sqlite3.connect('movies.db')

cursor = conn.cursor()

#cursor.execute("SELECT * FROM movies;")
#for row in cursor:
    #print(row)

#opdracht 1:
cursor.execute('''CREATE TABLE IF NOT EXISTS movies (
               id INTEGER PRIMARY KEY,
               title TEXT,
               year INTEGER
               )''')

#foutmelding door een komma teveel :')


cursor.execute('''INSERT INTO movies(id, title, year)
                  VALUES(80684,"Star Wars: Episode V - The Empire Strikes Back", 1980)''')

cursor.execute('''INSERT INTO movies(id, title, year)
                  VALUES(86190,"Star Wars: Episode VI - Return of the Jedi", 1983)''')

cursor.execute('''INSERT INTO movies(id, title, year)
                  VALUES(120915,"Star Wars: Episode I - The Phantom Menace", 1999)''')

cursor.execute('''INSERT INTO movies(id, title, year)
                  VALUES(121765,"Star Wars: Episode II - Attack of the Clones", 2002)''')

cursor.execute('''INSERT INTO movies(id, title, year)
                  VALUES(121766,"Star Wars: Episode III - Revenge of the Sith", 2005)''')

cursor.execute("SELECT * FROM movies WHERE title LIKE 'Star Wars%'")

for row in cursor:
    print(row)
