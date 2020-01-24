'''
Demo for listing records from database table
'''
import sqlite3

def display_people():
    sql_cmd = 'select * from people'
    with sqlite3.connect('mydb.sqlite3') as conn:
        cur = conn.cursor()
        cur.execute(sql_cmd)
        data = cur.fetchone()
        print('type of data is', type(data))
        print('data is', data)

        while True:
            data = cur.fetchone()
            if data==None: break
            print('data is', data)

        # for p in cur.fetchall():
        #     print(p)

def main():
    display_people()

if __name__=='__main__': main()