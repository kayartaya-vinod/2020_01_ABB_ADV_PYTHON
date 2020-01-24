'''
Demo to create a new table called 'people' in an SQLite3 database.
'''

from sqlite3 import connect

sql_cmd = '''create table people(
    id integer primary key autoincrement,
    name varchar(50) not null,
    gender varchar(10) default 'Male',
    email varchar(100) not null unique
)
'''
# open a connection to SQLite3 database
conn = connect('mydb.sqlite3')
cur = conn.cursor()

try:
    cur.execute(sql_cmd)
    print('Table people created!')
except Exception as ex:
    print('Table people could not be created!')
    print(ex)
finally:
    conn.close()
