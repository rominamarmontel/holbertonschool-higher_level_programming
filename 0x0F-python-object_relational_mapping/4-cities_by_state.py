#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    connection = MySQLdb.connect(host="localhost", port=3306, user=arg[1],
                                 passwd=arg[2], db=arg[3], charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    connection.close()
