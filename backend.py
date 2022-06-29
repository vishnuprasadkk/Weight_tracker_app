import sqlite3
from datetime import date
from anyio import connect_tcp
from sqlalchemy import null


def connect():

    conn=sqlite3.connect("counter.db")
    c=conn.cursor()
    c.execute('CREATE TABLE IF NOT EXISTS tracker(unique_id INTEGER PRIMARY KEY, weight FLOAT, current_date DATE)')
    conn.commit()
    conn.close()

def add(weight,current_date,):
    conn=sqlite3.connect("counter.db")
    c=conn.cursor()
    c.execute("INSERT INTO tracker VALUES(NULL,?,?)", (weight,current_date))
    conn.commit()
    conn.close()


def view():
    conn=sqlite3.connect("counter.db")
    c=conn.cursor()
    c.execute("SELECT * FROM tracker")
    rows=c.fetchall()
    conn.commit()
    conn.close()
    return rows





def delete_last_entry():
    conn=sqlite3.connect("counter.db")
    c=conn.cursor()
    c.execute("SELECT unique_id from tracker")
    ids=c.fetchall()
    x=ids[-1]
    c.execute("DELETE FROM tracker WHERE unique_id=?",(x))
    conn.commit()
    conn.close()






