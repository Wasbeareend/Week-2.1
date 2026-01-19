import sqlite3

conn = sqlite3.connect('movies.db')

cursor = conn.cursor()

#opdracht 2

cursor.execute('''INSERT OR IGNORE INTO people(id, name, birth)
                  VALUES(191, "Ewan Gordon McGregor", 1971)''')

cursor.execute('''INSERT OR IGNORE INTO people(id, name, birth)
                  VALUES(204, "Natalie Portman", 1981)''')

cursor.execute('''INSERT OR IGNORE INTO people(id, name, birth)
                  VALUES(159789, "Hayden Christensen", 1981)''')

cursor.execute('''INSERT OR IGNORE INTO people(id, name, birth)
                  VALUES(184, "George Lucas", 1944)''')

cursor.execute("SELECT name FROM people WHERE id IN (191, 204, 159789, 184)")

for row in cursor:
    print(row)

##gezien ik extreem veel errors kreeg: https://www.geeksforgeeks.org/sql/sql-insert-ignore-statement/