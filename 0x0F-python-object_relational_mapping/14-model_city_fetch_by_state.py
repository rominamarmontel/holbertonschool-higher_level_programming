#!/usr/bin/python3
"""Start link class to table in database
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from model_city import City
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        sys.argv[1],
        sys.argv[2],
        sys.argv[3]),
        pool_pre_ping=True)
    Base.metadata.create_all(engine)

    session = Session(engine)
    for city, State in session.query(City, State).join(State).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
    session.close()
