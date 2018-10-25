from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import settings

#Map a class that defines our table structure to Postgres as well as a function that will take our metadata of our table to create the table(s) we need
DeclarativeBase = declarative_base()

def db_connect():
	#Performs database connection using database settings from settins.py
	#Returns sqkakchent engine instance

	#The URL function, a constructor defined within SQLAlchemy, will map keys and values to a URL that SQLAlchemy can understand to make a conneciton to our database
	return create_engine(URL(**settings.DATABASE))

def create_items_table(engine):
	DeclarativeBase.meta.create_all(engine)

class Items(DeclarativeBase):
	#sqlalchemy items model
	_tablename_ = "RightMove"

	name = Column('Name', String)
	price = Column('Price', String, nullable = True)
	#category = Field()
	#propertyType = Field()
	address = Column('Adress', String, nullable = True)
	#itemId = Field() 
	#size = Field()
	description = Column('Description', String)