#!/usr/bin/python3

"""
  Script that takes an input from user
  and makes a query to the database
  but also safe from SQLinjection
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    """Takes an input but safely"""
    db = MySQLdb.connect(
            host='localhost', port=3306, user=argv[1], passwd=argv[2],
            db=argv[3])

    cursor = db.cursor()

    sql_query = "SELECT * FROM states WHERE name LIKE BINARY %s \
    ORDER BY id ASC"

    cursor.execute(sql_query, (argv[4] + '%',))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
