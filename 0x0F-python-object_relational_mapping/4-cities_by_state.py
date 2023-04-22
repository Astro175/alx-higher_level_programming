#!/usr/bin/python3

"""
  Script that takes a query and execute
"""
import MySQLdb
from sys import argv
if __name__ == '__main__':

    db = MySQLdb.connect(
            host='localhost', port=3306, user=argv[1],
            passwd=argv[2], db = argv[3])
    cursor = db.cursor()

    mysql_query = 'SELECT  FROM cities JOIN states \
    ON cities.state_id = states.id ORDER BY cities.id ASC'

    cursor.execute(mysql_query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)
