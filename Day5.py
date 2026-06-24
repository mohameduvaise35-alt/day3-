1. Create a Circle class and calculate area.

2. Create a Book class with title and author and display details.

3. Create a Person class and a Student class that inherits from it.

4. Create a School class with a class variable school_name and display it using a class method.

5.Rectangle Area
	Create a Rectangle class with:
	length
	breadth 
        Create a method area() to calculate and print the area.

6.Create Library management System application using class & Object and instance methods
_____________________________________
1.import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Area =", 3.14* self.radius ** 2)

c = Circle(5)
c.area()

2.
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
    def display(self):
        print("Title:", self.title)
        print("Author:", self.author)
b = Book("Python Basics", "John")
b.display()

3.
class person:
    def __init__ (self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("Name:",self.name)
        print("rollno:",self.rollno)
class student(person):
    pass
s=student("ravi",31)   
s.display()

4.
class School:
    school_name = "Nehru School of education"   

    @classmethod
    def display_school(cls):     
        print(cls.school_name

5.
class rectangle:
    def __init__(self, length, breadth ):
        self.length=length 
        self.breadth=breadth
    def area(self): 
        print("Area:",self.length*self.breadth)
a=rectangle(20,5)   
a.area()

6.
class library:
   def __init__(self):
    self.books=[]
    
   def add_book(self,book):
        self.book=book
        print(book,"is added ")
    
   def show_books(self):
        print("Books in Library ")
        for book in self.books:
            print(book)
lib=library()

lib.add_book("python")
lib.add_book("java")
lib.add_book("C++")

lib.show_books()
