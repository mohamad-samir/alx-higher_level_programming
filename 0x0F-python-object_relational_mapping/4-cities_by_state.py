#!/usr/bin/python3
"""
Lists all values in the states table of hbtn_0e_0_usa where name matches the argument (safe from MySQL injection)
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
        "SELECT * FROM states WHERE name = %s ORDER BY id",
        (state_name,)
    )

    rows = cursor.fetchall()
    for row in rows:
        print(row)
