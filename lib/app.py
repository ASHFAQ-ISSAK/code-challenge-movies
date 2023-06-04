import os
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Actor, Movie, Role

engine = create_engine("sqlite:///lib/db/movies.db")
Session = sessionmaker(bind=engine)
session = Session()


def create_movie():
    movie_title = input("Enter the movie title: ")
    box_office_earnings = int(input("Enter the box office earnings: "))
    actor_name = input("Enter the actor name: ")
    character_name = input("Enter the character name: ")
    salary = int(input("Enter the salary: "))

    movie = Movie(title=movie_title, box_office_earnings=box_office_earnings)
    actor = Actor(name=actor_name)
    role = Role(movie=movie, actor=actor, character_name=character_name, salary=salary)

    session.add(movie)
    session.add(actor)
    session.add(role)
    session.commit()


def get_actors():
    actors = session.query(Actor).join(Role).distinct(Actor.name).all()
    return actors


def get_movies():
    movies = session.query(Movie).join(Role).distinct(Movie.title).all()
    return movies


def get_roles(movie_title):
    roles = session.query(Role).join(Movie).filter(Movie.title == movie_title).all()
    return roles


def main():
    while True:
        option = input("Enter 'a' to add a movie or 'q' to quit: ")
        if option == "q":
            break
        elif option == "a":
            create_movie()
            print("Movie added successfully!")
        else:
            print("Invalid option. Please try again.")

    session.close()
    print("Exiting the program.")


if __name__ == "__main__":
    main()

    # Prompt the user for information
    command = input("Enter a command: ")

    # Handle the command
    if command == "Role actor":
        actors = get_actors()
        for actor in actors:
            print(f"Actor: {actor.name}")
    elif command == "Role movie":
        movies = get_movies()
        for movie in movies:
            print(f"Movie: {movie.title}")
    elif command == "Movie roles":
        movie_title = input("Enter the movie title: ")
        roles = get_roles(movie_title)
        for role in roles:
            print(f"Role: {role.character_name}")
