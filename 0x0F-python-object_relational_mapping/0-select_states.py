#!/usr/bin/python3
"""
  This script prints states from a database
"""
import sys
import MySQLdb
if __name__ == '__main__':
    """ Uses a cursor object to query"""
    us = sys.argv[1]
    ps = sys.argv[2]
    dbs = sys.argv[3]

    db = MySQLdb.connect(
            host='localhost', port=3306, user=us, passwd=ps, db=dbs)
    cursor = db.cursor()

    cursor.execute('SELECT * FROM states ORDER BY id ASC')

    rows = cursor.fetchall()

    for row in rows:
        print(row)
