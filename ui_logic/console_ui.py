import sys

from providers.data_provider_interface import DataProvider

ACTION_ITEMS = """
Choose action item from the list:
    1. add author
    2. add book
    3. add genre
    4. add book genre
    5. get books by genre
    6. get books by author and year
    7. get genre count
    8. exit
"""


class ConsoleDbApp:
    def __init__(self, raw_data_provider: type[DataProvider], orm_data_provider: type[DataProvider]) -> None:
        self.data_provider = None
        self.raw_data_provider = raw_data_provider
        self.orm_data_provider = orm_data_provider

    def start_app(self):
        choose = input('Choose data provider for initialization: 1 - raw, 2 - orm')
        self.data_provider = self.raw_data_provider if choose == '1' else self.orm_data_provider

        print('Starting Console Db App ...')
        self.data_provider.create_database_if_not_exist()
        self.data_provider.create_tables_if_not_exist()

        while True:
            action_item = int(input(ACTION_ITEMS))


            match action_item:
                case 1:
                    self.add_author()
                case 2:
                    self.add_book()
                case 3:
                    self.add_genre()
                case 4:
                    self.add_book_genre()
                case 5:
                   self.add_books_by_genre()
                case 6:
                    self.get_books_by_author_and_year()
                case 7:
                    self.get_genre_count()
                case 8:
                    print('Finishing work...')
                    sys.exit(0)

            input('Press enter to continue')

    def add_author(self):
        author_name = input('Please enter author name: ')
        author_id = self.data_provider.add_author(author_name)
        print(f'Author {author_name} created with id: {author_id}')


    def add_book(self):
        title, publication_year, author_id = input('Please enter title, /'
                                                   'publication_year, author_id: ').split(', ')
        book_id = self.data_provider.add_book(title, publication_year, author_id)
        print(f'Book {title} created with id: {book_id}')
    def add_genre(self):
        genre_name = input('Please enter genre name: ')
        genre_id = self.data_provider.add_genre(genre_name)
        print(f'Genre was created with id: {genre_id}')
    def add_book_genre(self):
        book_id, genre_id = input('Please enter book_id and genre_id: ').split(', ')
        created_book_id, created_genre_id = self.data_provider.add_book_genre(book_id, genre_id)
        print(f'Book with {created_book_id} was added to genre with {created_genre_id}')
    def add_books_by_genre(self):
        genre = input("Input genre_name: ")
        books = self.data_provider.get_books_by_genre(genre)

        if books:
            for book in books:
                print(f"Book title: {book[0]}")
        else:
            print("No books found for this genre.")

    def get_books_by_author_and_year(self):
        author_name = input("Input author_name: ")
        books = self.data_provider.get_books_by_author_and_year(author_name)
        if books:
            for title, year in books:
                print(f"{title} ({year})")
        else:
            print("No books found for this author.")

    def get_genre_count(self):
        results = self.data_provider.get_genre_count()
        for genre, count in results:
            print(f"Genre: {genre}, Number of books: {count}")