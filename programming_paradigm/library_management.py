# library_management.py

class Book:
    """
    Represents a single book in the library.
    Each book has a title, an author, and an availability status.
    """

    def __init__(self, title, author):
        """
        Initialize a new Book object.

        :param title: str, the book's title
        :param author: str, the book's author
        """
        self.title = title               # public attribute for the book's title
        self.author = author             # public attribute for the book's author
        self._is_checked_out = False     # private flag for checkout status

    def check_out(self):
        """
        Mark the book as checked out if it is available.

        :return: str, a message indicating success or that it was already checked out
        """
        if not self._is_checked_out:
            self._is_checked_out = True
            return f"'{self.title}' has been checked out."
        return f"'{self.title}' is already checked out."

    def return_book(self):
        """
        Mark the book as returned if it was checked out.

        :return: str, a message indicating success or that it wasn't checked out
        """
        if self._is_checked_out:
            self._is_checked_out = False
            return f"'{self.title}' has been returned."
        return f"'{self.title}' was not checked out."

    def is_available(self):
        """
        Check if the book is available for checkout.

        :return: bool, True if the book is not checked out, False otherwise
        """
        return not self._is_checked_out


class Library:
    """
    Manages a collection of Book instances.
    Allows adding books, checking out, returning, and listing available books.
    """

    def __init__(self):
        """
        Initialize the library with an empty list of books.
        """
        self._books = []  # private list to store Book objects

    def add_book(self, book):
        """
        Add a new Book to the library's collection.

        :param book: Book instance to add
        :return: str, confirmation message
        """
        self._books.append(book)
        return f"'{book.title}' by {book.author} has been added to the library."

    def list_available_books(self):
        """
        Print all books that are currently available (not checked out).
        """
        print("Available books:")
        for book in self._books:
            if book.is_available():
                print(f"- {book.title} by {book.author}")

    def check_out_book(self, title):
        """
        Find a book by title and attempt to check it out.

        :param title: str, the title of the book to check out
        :return: str, message indicating result
        """
        for book in self._books:
            if book.title == title:
                # Delegate the checkout logic to the Book instance
                return book.check_out()
        return f"Book titled '{title}' not found in the library."

    def return_book(self, title):
        """
        Find a book by title and attempt to return it.

        :param title: str, the title of the book to return
        :return: str, message indicating result
        """
        for book in self._books:
            if book.title == title:
                # Delegate the return logic to the Book instance
                return book.return_book()
        return f"Book titled '{title}' not found in the library."
