#!/usr/bin/python3

# This script lists all states with a name starting with 'N'
# from the database hbtn_0e_0_usa. Results are sorted by states.id in ascending order.

import MySQLdb
import sys

# Get MySQL username, password and database name from command line arguments
username = sys.argv[1]
password = sys.argv[2]
database = sys.argv[3]

# Connect to MySQL server on localhost at port 3306
db = MySQLdb.connect(host="localhost", port=3306,
                     user=username, passwd=password, db=database)
cursor = db.cursor()

# Execute SQL query to select states where name starts with 'N' and order by id
cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

# Fetch all the resulting rows
rows = cursor.fetchall()

# Print each row
for row in rows:
    print(row)

# Close the cursor and the database connection
cursor.close()
db.close()

