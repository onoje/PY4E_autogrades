# http://sqlite.org/
# http://sqlitebrowser.org/
# http://www.sqlite.org/datatypes.html
# http://www.py4e.com/code3/db1.py
# http://en.wikipedia.org/wiki/SQL
# http://www.py4e.com/code3/db2.py
# http://www.py4e.com/code3/twspider.py
# http://en.wikipedia.org/wiki/Relational_model
# http://www.py4e.com/code3/twfriends.py
# http://www.py4e.com/code3/twjoin.py


"""
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()
# A cursor is like a file handle that we can use to perform operations on the data stored in the database.

cur.execute('DROP TABLE IF EXISTS Track')
# DROP TABLE command deletes the table and all of its contents from the database.
cur.execute('CREATE TABLE Track (title TEXT, plays INTEGER)')

conn.close()
"""

"""
import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

# we can put some data into that table using the SQL INSERT operation.
cur.execute('INSERT INTO Track (title, plays) VALUES (?, ?)',
    ('Thunderstruck', 20))
cur.execute('INSERT INTO Track (title, plays) VALUES (?, ?)',
    ('My Way', 15))
conn.commit()
# use commit() to force the data to be written to the database file.

print('Track:')
cur.execute('SELECT title, plays FROM Track')
for row in cur:
     print(row)

cur.execute('DELETE FROM Track WHERE plays < 100')
conn.commit()

cur.close()
"""
