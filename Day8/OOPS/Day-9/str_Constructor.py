class Book:
    def __init__(self, title):
        print("Constructor Called")
        self.title = title
    def __str__(self):
      return f"Your Book is {self.title}"
book1 = Book("The Great Gatsby")
book2 = Book("GOAT")
print(book1)
print(book2)