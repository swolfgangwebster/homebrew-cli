#!/usr/bin/env python3


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from helpers import menuAndSelect, mainMenu, addCreator, createItem, assignCreator


if __name__ == '__main__':
    engine =  create_engine('sqlite:///db/homebrew.db')

    Session = sessionmaker(bind=engine)
    session = Session()

   # assignCreator(session)
    menuAndSelect(mainMenu, session)




    # addCreator(session)
    # createItem(session)

    
