#!/usr/bin/python3
'''
Script that prints the State object with the name passed as
argument from the database hbtn_0e_6_usa
'''

if __name__ == '__main__':
    import sys
    from model_state import State, Base
    from sqlalchemy import create_engine
    from sqlalchemy.orm import Session

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)

    state_search = sys.argv[4]
    Base.metadata.create_all(engine)

    session = Session(engine)

    state = session.query(State).filter(State.name == state_search)\
        .first()

    if state:
        print('{}'.format(state.id))
    else:
        print('Not found')

    session.close()
