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
def create_table(table_name):
    cur.execute('CREATE TABLE IF NOT EXISTS ?',(table_name))
    #if not exists so you can avoid deleting a previous table
    conn.commit()
    conn.close()

    #always close after a commit


