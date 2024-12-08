from sqlalchemy import create_engine, text, func
from sqlalchemy.orm import sessionmaker


from config import DB_NAME, DB_USER, DB_PASSWORD, DB_HOST, DB_PORT
from providers.data_provider_interface import DataProvider

DATABASE_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
SERVER_URI = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/postgres'


class SqlAlchemyProvider(DataProvider):
    connection = None

    @classmethod
    def get_connection(cls):
        pass


    @staticmethod
    def create_database_if_not_exist():
        pass


    @staticmethod
    def create_tables_if_not_exist():
        pass

    @staticmethod
    def add_author(author_name):
        pass

    @staticmethod
    def add_book(*args):
        pass

    @staticmethod
    def add_genre(genre_name):
        pass

    @staticmethod
    def add_book_genre(book_id, genre_id):
        pass

    @staticmethod
    def get_books_by_genre(genre_name):
        pass

    @staticmethod
    def get_books_by_author_and_year(author_name):
        pass

    @staticmethod
    def get_genre_count():
        pass