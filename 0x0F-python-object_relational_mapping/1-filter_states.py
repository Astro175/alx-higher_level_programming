#!/usr/bin/python3
"""Script that selects state with N"""
import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connects to the database and makes a query
    """
    us = sys.argv[1]
    ps = sys.argv[2]
    dbs = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost', port=3306, user=us, passwd=ps, db=dbs)

    cursor = db.cursor()

    cursor.execute(
            "SELECT * FROM states WHERE name LIKE BINARY \
                    'N%' ORDER BY states.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)
