#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """
import MySQLdb
import sys

if __name__ == '__main__':
    arg = sys.argv
    connection = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=arg[1],
        password=arg[2],
        db=arg[3],
        charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
