class Book:
    def __init__(self,title,author,isbn,publication_year):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = publication_year

    def get_age(self):
        current_year = 2025
        return current_year - self.publication_year
    
    def get_summary(self):
        return f"Title: {self.title}, Author: {self.author}, Published: {self.publication_year}"


Book1 = Book("OOPS Course", "Scott",1122334477, 2015)
Book2 = Book("Data Structures", "John",2211443366, 2018)

print("Book 1:", Book1.get_summary(), "AGE:", Book1.get_age())
print("Book 2:", Book2.get_summary(), "AGE:", Book2.get_age())