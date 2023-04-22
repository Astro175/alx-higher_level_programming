#!/usr/bin/python3
"""
  Script that takes state from user input
  and lists all cities from that state
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost',
                         port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name FROM cities JOIN \
            states ON cities.state_id = states.id WHERE \
            states.name = %s ORDER BY cities.id ASC",
                   (argv[4],))

    rows = cursor.fetchall()
    if rows is not None:
        print(", ".join([row[1] for row in rows]))
    cursor.close()
    db.close()
