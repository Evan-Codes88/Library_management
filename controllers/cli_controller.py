from flask import Blueprint
from datetime import date

from init import db
from models.member import Member
from models.author import Author
from models.book import Book
from models.genre import Genre
from models.loan import Loan



db_commands = Blueprint("db", __name__)

@db_commands.cli.command("create")
def create_tables():
    try:
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully.")
        

    except Exception as e:
        db.session.rollback()  # In case of error
        print(f"An error occurred while creating tables: {e}")
    

@db_commands.cli.command("drop")
def drop_tables():
    db.drop_all()
    print("Tables Dropped")

@db_commands.cli.command("seed")
def seed_tables():

    books = [
        Book(
            title = "The Fellowship Of The Ring",
            isbn = "978-0-261-10235-4",
            available_copies = 5,
            author_id = 1,
            genre_id = 1
        ),
        Book(
            title = "The Two Towers",
            isbn = "978-0-261-10236-1",
            available_copies = 3,
            author_id = 1,
            genre_id = 1
        ),
        Book(
            title = "The Return Of The King",
            isbn = "978-0-261-10237-8",
            available_copies = 5,
            author_id = 1,
            genre_id = 1
        ),
        Book(
            title = "The Final Empire",
            isbn = "978-0-7653-5037-4",
            available_copies = 5,
            author_id = 2,  
            genre_id = 1    
        ),
        Book(
            title = "The Well of Ascension",
            isbn = "978-0-7653-5612-4",
            available_copies = 4,
            author_id = 2,
            genre_id = 1
        ),
        Book(
            title = "The Hero of Ages",
            isbn = "978-0-7653-5613-1",
            available_copies = 5,
            author_id = 2,
            genre_id = 1
        ),
        Book(
            title = "The Way of Kings",
            isbn = "978-0-7653-2635-5",
            available_copies = 6,
            author_id = 2,
            genre_id = 1
        ),
        Book(
            title = "Words Of Radiance",
            isbn = "978-0-7653-2636-2",
            available_copies = 5,
            author_id = 2,
            genre_id = 1
        ),
         Book(
            title = "Oathbringer",
            isbn = "978-0-7653-2637-9",
            available_copies = 4,
            author_id = 2,
            genre_id = 1
        ),
        Book(
            title = "Rhythm of War",
            isbn = "978-0-7653-2638-6",
            available_copies = 3,
            author_id = 2,
            genre_id = 1
        ),
        Book(
            title = "Assassin's Apprentice",
            isbn = "978-0-553-37423-4",
            available_copies = 3,
            author_id = 3,
            genre_id = 1
        ),
        Book(
            title = "Gone Girl",
            isbn = "978-0-307-58836-4",
            available_copies = 7,
            author_id = 4,
            genre_id = 3
        ),
        Book(
            title = "Sharp Objects",
            isbn = "978-0-307-34156-3",
            available_copies = 4,
            author_id = 4,
            genre_id = 3
        ),
        Book(
            title = "The Shining",
            isbn = "978-0-385-12167-5",
            available_copies = 6,
            author_id = 5,
            genre_id = 6
        ),
        Book(
            title = "It",
            isbn = "978-1-5011-7688-6",
            available_copies = 2,
            author_id = 5,
            genre_id = 6
        ),
        Book(
            title = "Murder on the Orient Express",
            isbn = "978-0-00-711931-8",
            available_copies = 9,
            author_id = 6,
            genre_id = 5
        ),
        Book(
            title = "And Then There Were None",
            isbn = "978-0-06-207348-8",
            available_copies = 5,
            author_id = 6,
            genre_id = 5
        ),
        Book(
            title = "Fourth Wing",
            isbn = "978-0-346-47568-8",
            available_copies = 7,
            author_id = 7,  
            genre_id = 2
        ),
        Book(
            title = "Iron Flame",
            isbn = "978-0-346-47569-5",
            available_copies = 6,
            author_id = 7,
            genre_id = 2
        ),
        Book(
            title = "The Hunger Of The Gods",
            isbn = "978-0-316-70554-8",
            available_copies = 1,
            author_id = 8,
            genre_id = 1
        ),
        Book(
            title = "The Shadow Of The Gods",
            isbn = "978-0-316-54092-6",
            available_copies = 2,
            author_id = 8,
            genre_id = 1
        ),
        Book(
            title = "Harry Potter and the Philosopher's Stone",
            isbn = "978-0-7475-3269-6",
            available_copies = 2,
            author_id = 9,
            genre_id = 1
        ),
        Book(
            title = "Harry Potter And The Chamber Of Secret's",
            isbn = "978-0-7475-3849-1",
            available_copies = 9,
            author_id = 9,
            genre_id = 1
        ),
        Book(
            title = "Harry Potter and the Prisoner of Azkaban",
            isbn = "978-0-7475-4215-3",
            available_copies = 8,
            author_id = 9,
            genre_id = 1
        ),
    ]
    
    db.session.add_all(books)
    
    loans = [
        Loan(
            borrow_date = date(2024, 1, 12),
            return_date = date(2024, 12, 21),
            book_id = 1,
            member_id = 1
        ),
            Loan(
            borrow_date = date(2024, 12, 12),
            return_date = date(2024, 12, 30),
            book_id = 6,
            member_id = 3
        ),
            Loan(
            borrow_date = date(2024, 9, 12),
            return_date = date(2025, 5, 1),
            book_id = 18,
            member_id = 8
        ),
    ]
    db.session.add_all(loans)

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