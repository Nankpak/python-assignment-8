"""
TASK: Create a Library class.

Requirements:
1. The class should track available books (list).
2. Provide a method to add new books to the library.
3. Provide a method for users to borrow books.
   - Remove the borrowed book from available list.
   - Store borrowed books with user info.
4. Provide a method for returning borrowed books.
5. Provide a method to show all available books.

Example Usage:
    lib = Library()
    lib.add_book("Python 101")
    lib.add_book("Data Science Handbook")
    lib.borrow_book("Alice", "Python 101")
    print(lib.show_available_books())  # ["Data Science Handbook"]
    lib.return_book("Alice")
    print(lib.show_available_books())  # ["Data Science Handbook", "Python 101"]
"""
class Library:
    def __init__(self,books):
        self.books = {'nankpak':'csc111','tanfa':'python','polo':'java'}
        self.books.update({"npankpak":2222})
    def add_book(self,key,value):
        self.books.update({key:value})
        print(self.books)
    def borrow_book(self,borrow):
        if borrow in self.books:
            del self.books[borrow]
            print(self.books)
        else:
            print('book is not available')
    def available_books(self):
        for book in self.books:
            if self.borrow_book is not book:
                print(f'the available book is {self.books}')

library = Library('liberty')
library.add_book('don','java')
library.borrow_book('polo')
library.available_books()
        