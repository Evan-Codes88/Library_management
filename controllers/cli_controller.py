from flask import Blueprint

from init import db
from models.author import Author
from models.genre import Genre
from models.member import Member

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
    
    members = [
        Member(
            name = "Alice Smith",
            membership_number = "10001111",
            email = "alice.smith@example.com",
            join_date = "2022-01-15"
        ),
        Member(
            name = "Bob Johnson",
            membership_number = "10001112",
            email = "bob.johnson@example.com",
            join_date = "2022-01-10"
        ),
        Member(
            name = "Charlie Brown",
            membership_number = "10001113",
            email = "charlie.brown@example.com",
            join_date = "2022-03-05"
        ),
        Member(
            name = "Ethan Hunt",
            membership_number = "10001114",
            email = "ethan.hunt@example.com",
            join_date = "2023-12-04"
        ),
        Member(
            name = "Wilson Jefferson",
            membership_number = "10001115",
            email = "wilson.jefferson@example.com",
            join_date = "2024-08-12"
        ),
        Member(
            name = "Ian Wright",
            membership_number = "10001116",
            email = "ian.wright@example.com",
            join_date = "2007-05-22"
        ),
        Member(
            name = "Rachael Green",
            membership_number = "10001117",
            email = "rachael.green@example.com",
            join_date = "2013-02-07"
        ),
        Member(
            name = "Peter Parker",
            membership_number = "10001118",
            email = "peter.parker@example.com",
            join_date = "2008-11-15"
        ),
        Member(
            name = "Clark Kent",
            membership_number = "10001119",
            email = "clark.kent@example.com",
            join_date = "2018-08-12"
        ),
        Member(
            name = "Bruce Wayne",
            membership_number = "10001120",
            email = "bruce.wayne@example.com",
            join_date = "2006-01-01"
        ),
        Member(
            name = "Bruce Banner",
            membership_number = "10001121",
            email = "bruce.banner@example.com",
            join_date = "2015-04-12"
        ),
        Member(
            name = "Tony Stark",
            membership_number = "10001122",
            email = "tony.stark@example.com",
            join_date = "2020-07-18"
        )
    ]
    
    db.session.add_all(members)
    db.session.commit()
    print("Tables Seeded")