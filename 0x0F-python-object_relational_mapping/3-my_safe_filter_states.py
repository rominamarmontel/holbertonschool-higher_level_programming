#!/usr/bin/python3
"""takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    connection = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                                 passwd=arg[2], db=arg[3], charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE Name = %s ORDER BY id ASC",
                   (argv[4],))
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
