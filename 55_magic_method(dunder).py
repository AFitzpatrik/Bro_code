#Magic methods = dunder methods (__ double underscore), __init__, __str__, __eq__
#               They are automatically canlled by many Pythons built in operations.
#               They allow developers to define or customize the behavior of objects.




class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"{self.title} by {self.author}." #string representation of the object, we can print it(otherwise it would print the


    def __eq__(self, other):#equals, self and other book
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):#less than
        return self.num_pages < other.num_pages


    def __gt__(self, other):
        return self.num_pages > other.num_pages



    def __add__(self, other):
        return self.num_pages + other.num_pages


    def __contains__(self, keyword): #hledání slova v objektu
        return keyword in self.title


    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
           return f"Key '{key}' not found in the book object."

book1 = Book("The Hobbit", "J.R.R. Tolkien", 310) #instance třídy BOOK
book2 = Book("Harry Potter and the Philosopher's Stone", "J.K. Rowling", 223) #instance třídy BOOK
book3 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172) #instance třídy BOOK
book4 = Book("The Lion, the Witch and the Wardrobe", "C.S. Lewis", 172)

print(book1)
print(book3 == book4)
print(book4 < book1)
print(book1 > book2)
print(book1 + book2)
print("Lion" in book3)
print(book1['title']) #print title of the book
print(book1['author'])
print(book1['num_pages'])
print(book1['audiot'])