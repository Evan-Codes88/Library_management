from flask import Blueprint

from init import db
from models.author import Author
from models.genre import Genre

db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    db.create_all()
    print("Tables Created")

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables Dropped")

@db_commands.cli.command("seed")
def seed_tables():

    authors = [
        Author(
            name = "J.R.R. Tolkein",
            birth_year = 1892
        ),
        Author(
            name = "Brandon Sanderson",
            birth_year = 1975
        ),
        Author(
            name = "Robin Hobb",
            birth_year = 1952
        ),
        Author(
            name = "Gillian Flynn",
            birth_year = 1971
        ),
        Author(
            name = "Stephen King",
            birth_year = 1947
        ),
        Author(
            name = "Agatha Christie",
            birth_year = 1890
        ),
        Author(
            name = "Rebecca Yarros",
            birth_year = 1981
        ),
        Author(
            name = "John Gwynne",
            birth_year = 1968
        ),
        Author(
            name = "J.K. Rowling",
            birth_year = 1965
        ),
    ]

    db.session.add_all(authors)

    genres = [
        Genre(
            genre_name = "Fantasy"
        ),
        Genre(
            genre_name = "Romantasy"
        ),
        Genre(
            genre_name = "Thriller"
        ),
        Genre(
            genre_name = "Romance"
        ),
        Genre(
            genre_name = "Murder Mystery"
        ),
        Genre(
            genre_name = "Horror"
        ),
        Genre(
            genre_name = "Adventure"
        ),
        Genre(
            genre_name = "Science Fiction"
        ),
    ]
    db.session.add_all(genres)
    db.session.commit()
    print("Tables Seeded")