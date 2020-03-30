#!/usr/bin/python3
""" List all states """

from sys import argv
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                               port=3306,
                               user=argv[1],
                               passwd=argv[2],
                               db=argv[3])
    cur = db.cursor()
    query = """
    SELECT cities.name FROM cities
    JOIN states ON cities.state_id = states.id WHERE states.name=%s
    ORDER BY cities.id ASC;
    """
    cur.execute(query,(argv[4],))
    rows = cur.fetchall()
    cities = [row[0] for row in rows]
    print(', '.join(cities))
    cur.close()
    db.close()
