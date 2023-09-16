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
    arg: str = sys.argv[4]
    host: str = "localhost"
    port: int = 3306

    statement: str = """
    SELECT c.id, c.name, s.name
    FROM cities AS c
    JOIN states AS s
    ON c.state_id = s.id
    HAVING BINARY s.name = %s
    ORDER BY c.id;
    """

    db = MySQLdb.connect(
        user=username,
        host=host,
        port=port,
        password=password,
        database=db_name,
    )
    cursor = db.cursor()

    cursor.execute(statement, (arg,))
    rows = cursor.fetchall()
    cities = tuple(row[1] for row in rows)
    cities = ', '.join(cities)
    print(cities)
