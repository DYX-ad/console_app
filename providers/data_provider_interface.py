from abc import ABC, abstractmethod


class DataProvider(ABC):
    @classmethod
    @abstractmethod
    def get_connection(cls):
        pass

    @staticmethod
    @abstractmethod
    def create_database_if_not_exist():
        pass

    @staticmethod
    @abstractmethod
    def create_tables_if_not_exist():
        pass

    @staticmethod
    @abstractmethod
    def add_author(author_name):
        pass

    @staticmethod
    @abstractmethod
    def add_book(*args):
        pass

    @staticmethod
    @abstractmethod
    def add_genre(genre_name):
        pass

    @staticmethod
    @abstractmethod
    def add_book_genre(book_id, genre_id):
        pass

    @staticmethod
    @abstractmethod
    def get_books_by_genre(genre_name):
        pass

    @staticmethod
    @abstractmethod
    def get_books_by_author_and_year(author_name):
        pass

    @staticmethod
    @abstractmethod
    def get_genre_count():
        pass