class Library:
    def __init__(self, booklist)
        self.available=booklist

    def display_available_books(self):
        for book in self.available:
            print(book)
    
    def lend_book(self,requested_book):
        if requested_book in self.available:
            print("Book borrowed, date: ")
        else:
            print("Book unavailable")

class Book:
    def __init__(self, title, author, ISBN_number):
        self.title=title
        self.author=author
        self.ISBN_number=ISBN_number
        self.is_available=True
