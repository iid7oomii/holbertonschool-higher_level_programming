#!/usr/bin/python3
"""
This script lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa. Results are sorted by states.id in ascending order.
It takes 3 arguments: mysql username, mysql password, and database name.
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC;")
    for state in cursor.fetchall():
        print(state)
    cursor.close()
    db.close()
