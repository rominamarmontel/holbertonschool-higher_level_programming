#!/usr/bin/python3
"""takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    connection = MySQLdb.connect(
        host="localhost",
        port=3306, user=arg[1],
        passwd=arg[2],
        db=arg[3],
        charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{:s}'"
                   .format(arg[4],))
    rows = cursor.fetchall()
    for row in rows:
        if row[1] == arg[4]:
            print(row)
    cursor.close()
    connection.close()
