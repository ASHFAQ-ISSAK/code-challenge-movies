import os
import sys
from sqlalchemy import create_engine, Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine("sqlite:///lib/db/movies.db", echo=True)


class Actor(Base):
    __tablename__ = "actors"
    id = Column(Integer, primary_key=True)
    name = Column(String())  # Add this line

    def __repr__(self):
        return f"Actor: {self.name}"


class Movie(Base):
    __tablename__ = "movies"
    id = Column(Integer, primary_key=True)
    title = Column(String())
    box_office_earnings = Column(Integer())
    actors = relationship("Role", back_populates="movie")

    def __repr__(self):
        return f"Movie: {self.title}"


class Role(Base):
    __tablename__ = "roles"
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey("movies.id"))
    actor_id = Column(Integer, ForeignKey("actors.id"))
    salary = Column(Integer())
    character_name = Column(String())
    movie = relationship("Movie", back_populates="actors")
    actor = relationship("Actor")

    def __repr__(self):
        return f"Role: {self.character_name}"

    @classmethod
    def get_actors(cls):
        return session.query(cls.actor).distinct().all()

    @classmethod
    def get_movies(cls, engine):
        Session = sessionmaker(bind=engine)
        session = Session()
        movies = session.query(Role.movie).distinct().all()
        return movies


Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Prompt the user for information
movie_title = input("Enter the movie title: ")
box_office_earnings = int(input("Enter the box office earnings: "))
actor_name = input("Enter the actor name: ")
character_name = input("Enter the character name: ")
salary = int(input("Enter the salary: "))

# Create the objects
movie = Movie(title=movie_title, box_office_earnings=box_office_earnings)
actor = Actor(name=actor_name)
role = Role(movie=movie, actor=actor, character_name=character_name, salary=salary)

# Add objects to the session
session.add(movie)
session.add(actor)
session.add(role)

# Commit the changes
session.commit()

# Close the session
session.close()


Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Prompt the user for information
movie_title = input("Enter the movie title: ")
box_office_earnings = int(input("Enter the box office earnings: "))
actor_name = input("Enter the actor name: ")
character_name = input("Enter the character name: ")
salary = int(input("Enter the salary: "))

# Create the objects
movie = Movie(title=movie_title, box_office_earnings=box_office_earnings)
actor = Actor(name=actor_name)
role = Role(movie=movie, actor=actor, character_name=character_name, salary=salary)

# Add objects to the session
session.add(movie)
session.add(actor)
session.add(role)

# Commit the changes
session.commit()

# Close the session
session.close()
