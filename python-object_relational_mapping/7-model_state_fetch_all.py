#!/usr/bin/python3
"""
    Script to list all State object from database hbtn_0e_0_usa

    ARGUMENTS :
            mysql username
            mysql password
            database name
    SORTED BY :
        ASC states.id
"""

import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # create bd
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(sys.argv[1],
                sys.argv[2],
                sys.argv[3]),
        pool_pre_ping=True
    )
    # function to create all tables in the bd engine
    Base.metadata.create_all(engine)

    # create session to save in bd
    Session = sessionmaker(bind=engine)
    session = Session()

    # query + construct string response
    query = session.query(State.id, State.name)
    for row in query:
        print(str(row[0]) + ": " + row[1])
