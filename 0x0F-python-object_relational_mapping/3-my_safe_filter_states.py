#!/usr/bin/python3
""" List all states """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    state = argv[4]
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(query, (state, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    db.close()
