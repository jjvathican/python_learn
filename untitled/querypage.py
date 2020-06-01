import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()
#c.execute("INSERT INTO login VALUES ('jerin','pass')")
c.execute("drop table login")
conn.commit()
conn.close()
