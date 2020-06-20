# SQLITE DATABASE
#
#
# CONNECTING TO A DATABASE LOCALLY AND ALSO MANIPULATING DATA VIA A SCRIPT

import sqlite3

#creating a connection
conn = sqlite3.connect('day9.db')

#creating cursor
cur = conn.cursor()

#Function to create table
def create_table():
    cur.execute('CREATE TABLE IF NOT EXISTS test(NAME TEXT,SURNAME TEXT,ADDRESS TEXT)')
    #if not exists so you can avoid deleting a previous table
    conn.commit()
    conn.close()

    #always close after a commit

def update(name,surname,address):
    cur.execute('INSERT INTO test VALUES(?,?,?)',(name,surname,address))
    #The ? avoid sql injections in the future
    conn.commit()

    conn.close()





