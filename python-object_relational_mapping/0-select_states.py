#!/usr/bin/python3
"""
This script lists all states from the database hbtn_0e_0_usa
using MySQLdb. Results are sorted in ascending order by states.id.
"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Get arguments from command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server on localhost at port 3306
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=database)
    cursor = db.cursor()

    # Execute query to get all states sorted by id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close cursor and connection
    cursor.close()
    db.close()
