#!/usr/bin/python3
"""
Lists all State objects from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    host = "localhost"
    port = 3306

    # Setup SQLAlchemy engine and session
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@{host}/{db_name}', pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query for all State objects
    for state in session.query(State).order_by(State.id):
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
