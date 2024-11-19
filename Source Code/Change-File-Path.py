import os
import sqlite3

conn = sqlite3.connect('film_categories.db')
c = conn.cursor()

c.execute("SELECT *, oid FROM categories")
records = c.fetchall()

new_path = []
oid_list = []

for i in records:
	new_temp_path = "//username/folder-path" + i[1][2:]
	new_path.append(new_temp_path)
	oid_list.append(i[28])
conn.commit()
conn.close()

conn = sqlite3.connect('film_categories.db')
c = conn.cursor()
for i in range(len(new_path)):
	c.execute("""UPDATE categories SET
		film_path = :film_path
		WHERE oid = :oid""",
		{
		'film_path': new_path[i],
		'oid': oid_list[i]
		})
	print(oid_list[i])

conn.commit()
conn.close()