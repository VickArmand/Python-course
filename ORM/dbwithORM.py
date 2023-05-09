#!/usr/bin/env python3
from sqlalchemy import create_engine, Column, Integer,String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
"""
in this module we are demonstrating the use of sqlalchemy orm in sql database manipulation
"""
# connection to database
# in the command below we are passing the database connector as a parameter to the method create_engine to ensure connection
# the connector takes the following syntax:
# db_flavor(mysql or postgresql)+db_connector(mysqldb or pymysql)://user:password@host/db_name

# engine = create_engine('mysql+mysqldb://user:pwd@localhost/blogs', echo = True)
engine = create_engine('mysql+pymysql://user:pwd@localhost/blogs', echo = True)
print(f'Connection established {engine}')
# session creation - this is similar to the cursor creation in the other file
Session = sessionmaker(bind=engine)
session = Session()
print(f'Session created - {session}')

Base = declarative_base()
# The class below enlists the attributes which will lead to creation of the posts table
class Post(Base):
    __tablename__= 'posts'
    id = Column(Integer, primary_key = True)
    content = Column(String(100))

    def __repr__(self):
        return f"Post - {self.content}"
# Creating the table
Base.metadata.create_all(engine)
# Inserting our first post instance
post1 = Post(content = 'Hello World')
session.add(post1)
session.commit()
# fetching our records
query = session.query(Post)
print(query.all())