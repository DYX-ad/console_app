from providers.raw_sql_provider import RawSqlProvider


def main():

    print('Starting console app...')
    RawSqlProvider.create_database_if_not_exist()
    RawSqlProvider.create_tables_if_not_exist()

    author_name = input('Please enter author name: ')
    author_id = RawSqlProvider.add_author(author_name)
    print(f'Author {author_name} created with id: {author_id}')

    title, publication_year, author_id = input('Please enter title, publication_year, author_id: ').split(', ')
    book_id = RawSqlProvider.add_book(title, publication_year, author_id)
    print(f'Book {title} created with id: {book_id}')

    genre_name = input('Please enter genre name: ')
    genre_id = RawSqlProvider.add_genre(genre_name)
    print(f'Genre was created with id: {genre_id}')

    book_id, genre_id = input('Please enter book_id and genre_id: ').split(', ')
    created_book_id, created_genre_id = RawSqlProvider.add_book_genre(book_id, genre_id)
    print(f'Book with {created_book_id} was added to genre with {created_genre_id}')


    genre = input("Input genre_name: ")
    RawSqlProvider.get_books_by_genre(genre)


    author_name = input("Input author_name: ")
    RawSqlProvider.get_books_by_author_and_year(author_name)

    genre_count = RawSqlProvider.get_genre_count()


if __name__ == '__main__':
    main()