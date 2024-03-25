# https://www.py4e.com/code3/emaildb.py?PHPSESSID=1eae516bf0e0aad9e35492c614954fa0
# https://www.py4e.com/code3/mbox.txt?PHPSESSID=1eae516bf0e0aad9e35492c614954fa0
import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('''
CREATE TABLE IF NOT EXISTS Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if len(fname) < 1: fname = 'mbox.txt'
fh = open(fname)

for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    email = pieces[1]
    domain = email.split('@')[1]  # This part had an error but this line fix it
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain,))  # org had an error but it fixed
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (domain,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (domain,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

print("Counts:")
for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()
