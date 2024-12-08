from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Author(Base):
    __tablename__ = 'authors'
    author_id = Column(Integer, primary_key=True)
    author_name = Column(String, nullable=False)


class Genre(Base):
    __tablename__ = 'genres'
    genre_id = Column(Integer, primary_key=True)
    genre_name = Column(String, nullable=False)

class Book(Base):
     __tablename__ = 'books'
     book_id = Column(Integer, primary_key=True)
     title = Column(String, nullable=False)
     publicaion_year = Column(Integer)
     author_id = Column(Integer, ForeignKey('authors.author_id'))
     author = relationship('Author')

class BookGenre(Base):
     __tablename__ = 'book_genres'
     book_id = Column(Integer, ForeignKey('books.book_id'), primary_key=True)
     genre_id = Column(Integer, ForeignKey('genres.genre_id'), primary_key=True)
     book = relationship('Book')
     genre = relationship('Genre')
