#!/usr/bin/python3
"""
Lists all cities of a state from the database hbtn_0e_4_usa
using a state name provided as an argument
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username: str = sys.argv[1]
    password: str = sys.argv[2]
    db_name: str = sys.argv[3]
    state_name: str = sys.argv[4]
    host: str = "localhost"
    port: int = 3306

    db = MySQLdb.connect(
        user=username,
        host=host,
        port=port,
        password=password,
        database=db_name,
    )
    cursor = db.cursor()

    cursor.execute(
        "SELECT name FROM cities WHERE state_id IN (SELECT id FROM states WHERE name = %s) ORDER BY id",
        (state_name,)
    )

    rows = cursor.fetchall()
    cities = [row[0] for row in rows]
    print(", ".join(cities))
