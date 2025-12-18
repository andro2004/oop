class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        if book not in self.books:
            self.books.append(book)
            print(f'Book "{book}" added to the library.')
        else:
            print(f'Book "{book}" is already in the library.')

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
        else:
            print("Book is not in the library.")

    def list_books(self):
        print( "Books in the library:")
        for book in self.books:
            print(f"- {book}")
    
    def borrow_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f'You have borrowed "{book}".')
        else:
            print(f'"{book}" is not found in the library.')
    def return_book(self, book):
        self.books.append(book)
        print(f'You have returned "{book}".')
    