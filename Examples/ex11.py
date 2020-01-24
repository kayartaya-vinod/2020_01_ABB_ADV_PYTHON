'''
Demo for inserting records into the 'people' table
'''

import sqlite3

def add_person():
    name = input('Enter name: ')
    gender = input('Enter gender: ')
    email = input('Enter email: ')
    params = (name, gender, email)

    sql_cmd = 'insert into people(name, gender, email) values (?, ?, ?)'
    try:
        conn = sqlite3.connect('mydb.sqlite3')
        cur = conn.cursor()
        cur.execute(sql_cmd, params)
        conn.commit()
    except Exception as ex:
        print('ERROR: ', ex)

def main():
    while True:
        add_person()
        choice = input('Do you wish to continue? yes/no ') or 'yes'
        if choice!='yes': break
    print('Thank you, have a nice day!')

if __name__=='__main__': main()