# library_system.py
# Demonstrates inheritance (Book <- EBook, PrintBook) and composition (Library contains books)

from typing import List


# ---------------------------------------------------------------------
# Step 1 — Define the base class Book
# This class holds the common attributes shared by all books:
# - title (str)
# - author (str)
#
# It also provides a __str__ implementation to give a human-readable
# description. Derived classes can extend this behavior.
# ---------------------------------------------------------------------
class Book:
    """Base Book class with common attributes and behavior."""

    def __init__(self, title: str, author: str) -> None:
        # Initialize the common attributes for every Book instance.
        # We do not perform heavy validation here to keep the example simple,
        # but you could check types or non-empty strings if desired.
        self.title: str = title
        self.author: str = author

    def __str__(self) -> str:
        """
        Human-friendly string representation.
        Used by print(book) and str(book).
        """
        return f"Book: {self.title} by {self.author}"

    def __repr__(self) -> str:
        """
        Official representation useful for debugging; not required by the task
        but convenient when inspecting objects in REPL or logs.
        """
        return f"Book({self.title!r}, {self.author!r})"


# ---------------------------------------------------------------------
# Step 2 — Define derived class EBook
# EBook inherits from Book and adds file_size (int).
# Important: call super().__init__(title, author) to initialize the base class.
# ---------------------------------------------------------------------
class EBook(Book):
    """EBook extends Book with a file_size attribute (in KB)."""

    def __init__(self, title: str, author: str, file_size: int) -> None:
        # First initialize the shared Book attributes via the base class.
        super().__init__(title, author)

        # Then initialize the EBook-specific attribute.
        # We cast to int to be defensive if a numeric string is passed.
        self.file_size: int = int(file_size)

    def __str__(self) -> str:
        """
        Override __str__ to include the file size in the human-readable form.
        This demonstrates polymorphism: code that prints Book instances will
        automatically receive the right formatted string depending on the runtime type.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"

    def __repr__(self) -> str:
        return f"EBook({self.title!r}, {self.author!r}, {self.file_size})"


# ---------------------------------------------------------------------
# Step 3 — Define derived class PrintBook
# PrintBook inherits from Book and adds page_count (int).
# ---------------------------------------------------------------------
class PrintBook(Book):
    """PrintBook extends Book with a page_count attribute."""

    def __init__(self, title: str, author: str, page_count: int) -> None:
        # Initialize the shared Book attributes.
        super().__init__(title, author)

        # Initialize PrintBook-specific attribute.
        self.page_count: int = int(page_count)

    def __str__(self) -> str:
        # Polymorphic __str__ for printed books
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"

    def __repr__(self) -> str:
        return f"PrintBook({self.title!r}, {self.author!r}, {self.page_count})"


# ---------------------------------------------------------------------
# Step 4 — Define the Library class to demonstrate composition
# Library "has" books. It stores a list of Book (and subclasses) instances.
# - add_book(book): validates and stores a book
# - list_books(): iterates over stored books and prints their details
# ---------------------------------------------------------------------
class Library:
    """A simple Library class managing a collection of Book instances."""

    def __init__(self) -> None:
        # Initialize an empty list that will hold Book/EBook/PrintBook objects.
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """
        Add a book to the library.

        Step-by-step:
        1. Validate that the object is an instance of Book (or subclass).
        2. Append it to the internal list.
        """
        if not isinstance(book, Book):
            # Defensive programming: only Book-like objects are allowed.
            raise TypeError("add_book expects an instance of Book, EBook, or PrintBook")
        self.books.append(book)

    def list_books(self) -> None:
        """
        Print details of each book in the library.

        Note:
        We rely on polymorphism: each book's __str__ method will produce
        the appropriate line (Book, EBook, or PrintBook) when printed.
        """
        if not self.books:
            print("The library has no books.")
            return

        for book in self.books:
            # print(book) calls the class-specific __str__ implementation.
            print(book)
