#https://www.py4e.com/code3/mbox.txt
import sqlite3

#create database called emaildb
conn = sqlite3.connect('C4_W2_email_counter_DB.sqlite')
cur = conn.cursor()

#This will remove databse to prevent the code from blowing up
cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
#if (len(fname) < 1): fname = 'mbox-short.txt'
#fh = open(fname)
fh=open('/Users/JZ/Downloads/mailbox.txt')
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()
    e_1 = pieces[1]
    org = e_1.split('@')[1]
    # (email,) is a weird 1 tuple syntax in python3
    cur.execute('SELECT count FROM Counts WHERE org = ? ', (org,))
    row = cur.fetchone()
    if row is None:
        cur.execute('''INSERT INTO Counts (org, count)
                VALUES (?, 1)''', (org,))
    else:
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?',
                    (org,))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()

#python3 downloads/py4e/c4_w2_create_email_database.py
