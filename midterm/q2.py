class Book:
    def __init__(self, title: str, author: str, isbn: str):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def borrow_book(self):
        if not self.is_available:
            raise Exception("Book is already borrowed.")
        self.is_available = False

    def return_book(self):
        self.is_available = True

    def __str__(self):
        status = "Available" if self.is_available else "Borrowed"
        return f"Book Title: {self.title}, Author: {self.author}, Status: {status}"


class LibraryMember:
    def __init__(self, member_id: str, name: str):
        self.member_id = member_id
        self.name = name
        self.borrowed_books = []

    def borrow(self, book: Book):
        if not book.is_available:
            raise Exception("Book is already borrowed.")
        book.borrow_book()
        self.borrowed_books.append(book)

    def return_book(self, book: Book):
        if book not in self.borrowed_books:
            raise Exception("Book not found in borrowed list.")
        book.return_book()
        self.borrowed_books.remove(book)

    def __str__(self):
        borrowed_titles = [book.title for book in self.borrowed_books]
        return f"Member: {self.name}, Borrowed Books: {', '.join(borrowed_titles) if borrowed_titles else 'None'}"


class Library:
    def __init__(self, name: str):
        self.name = name
        self.books = []
        self.members = []

    def add_book(self, book: Book):
        self.books.append(book)

    def remove_book(self, book: Book):
        if book not in self.books:
            raise Exception("Book not found in library.")
        self.books.remove(book)

    def register_member(self, member: LibraryMember):
        self.members.append(member)

    def find_available_books(self):
        return [book for book in self.books if book.is_available]

    def __str__(self):
        return f"Library: {self.name}, Total Books: {len(self.books)}, Members: {len(self.members)}"


# Create library instance
library = Library("BAU Library")

# Create books
book1 = Book("1984", "George Orwell", "ISBN001")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "ISBN002")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", "ISBN003")

# Add books to library
library.add_book(book1)
library.add_book(book2)
library.add_book(book3)

# Create members
member1 = LibraryMember("M001", "Jack Shephard")
member2 = LibraryMember("M002", "Kate Austen")

# Register members
library.register_member(member1)
library.register_member(member2)

# Demonstrate borrowing and returning books
print(f"Available Books Before Borrowing: {[str(book) for book in library.find_available_books()]}")
member1.borrow(book1)
print(f"Available Books After Alice Borrows: {[str(book) for book in library.find_available_books()]}")
member1.return_book(book1)
print(f"Available Books After Alice Returns: {[str(book) for book in library.find_available_books()]}")
