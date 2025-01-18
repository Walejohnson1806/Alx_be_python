class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_out(self):
        if not self._is_checked_out:
            self._is_checked_out = True

        else:
            print(f"'{self.title}' is already checked out.")

    def return_book(self):
        if self._is_checked_out:
            self._is_checked_out = False

        else:
            print(f"'{self.title}' hasn't been returned.")

    def is_available(self):

        return not self._is_checked_out


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()
                return

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()

                return

    def list_available_books(self):
        if not self._books:
            print("No book available")
        else:

            for book in self._books:
                if book.is_available():
                    print(f"{book.title} by {book.author}")