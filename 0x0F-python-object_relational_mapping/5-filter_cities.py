#!/usr/bin/python3
"""takes in the name of a state as an argument
and lists all cities of that state"""

import MySQLdb
import sys

if __name__ == "__main__":
    arg = sys.argv
    connection = MYSQLdb.connect(host="localhost",
                                 port=3306,
                                 user=arg[1],
                                 password=arg[2],
                                 db=arg[3],
                                 charset="utf8")
    cursor = connection.cursor()
    cursor.execute("SELECT cities.name
    FROM cities
    JOIN states
    ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC", (arg[4],))
    query_rows = cursor.fetchall()
    array = []
    for row in query_rows:
        array.append(row[0])
    print(", ".join(array))
    cursor.close()
    connection.close()
