
#This is a simple library management system that allows you to add books and display the details of the library.
# It uses classes and instance variables to manage the library's state.

class Library:
    def __init__(self):
        self.NoBooks = 0
        self.books =[]

    def addBook(self, book):
        self.books.append(book)
        self.NoBooks = len(self.books)

    def showdetails(self):
        print(f"The library has {self.NoBooks} books. The Books are: ")
        for book in self.books:
            print(book)

l1 = Library()
l1.addBook("Basic Python")
l1.addBook("Lean Java-Script")
l1.addBook("Data Science")
l1.addBook("Machine Learning")
l1.showdetails()