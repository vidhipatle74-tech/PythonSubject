
#Multilevel inheritance==>>
"""
class School:

    def __init__(self, name, roll_no, course):
        self.name = name
        self.roll_no = roll_no
        self.course = course

    def show_data(self):
        print(f"The name of the student is {self.name}")
        print(f"The roll number of the student is {self.roll_no}")
        print(f"The course of the student is {self.course}")


class Twelth(School):

    def __init__(self, name, roll_no, course, marks, grade, position):
        super().__init__(name, roll_no, course)
        self.marks = marks
        self.grade = grade
        self.position = position

    def show_data(self):
        super().show_data()
        print(f"The marks of the student is {self.marks}")
        print(f"The grade of the student is {self.grade}")
        print(f"The position of the student is {self.position}")


class Degree(Twelth):

    def __init__(self, name, roll_no, course, marks, grade, position, degree):
        self.degree = degree
        super().__init__(name, roll_no, course, marks, grade, position)
        

    def show_data(self):
        super().show_data()
        print(f"The degree of the student is {self.degree}")


d = Degree("Vidhi", 101, "Python Full Stack", 75, "A", "1st", "BCA")

d.show_data()
"""
#o/p--> The name of the student is Vidhi
#            The roll number of the student is 101
#            The course of the student is Python Full Stack
#            The marks of the student is 75
#            The grade of the student is A
#            The position of the student is 1st
#            The degree of the student is BCA
    
#(1)single level inheritance-->>
"""
class  Vehicle:

    def start(self,Vname,Vtype):
        self.Vtype=types
        self.Vname=name

        print(f'The name of the vehicle is {self.Vname}')
        print(f'The type of the vehical is {self.Vtype}')

class Bike(Vehicle):

    def start(self,Vnumber,engine):
        self.Vnumber=Vnumber
        self.engine=engine

        print(f'The number of the vehicle is {self.Vnumber}')
        print(f'The engine of the bike is {self.engine}')

b=Bike()
b1=Bike()
b.start("car","thar")
b1.start("MH 35 T 4560","Special")
"""
#O/P--> The number of the vehicle is car
#             The engine of the bike is thar
#             The number of the vehicle is MH 35 T 4560
#             The engine of the bike is Special
 
#multiple Inheritance--->
"""
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def details(self):
        print(f"Name: {self.name}, Age: {self.age}")


class Company:
    def __init__(self, company_name, salary):
        self.company_name = company_name
        self.salary = salary

    def details(self):
        print(f"Company: {self.company_name}, Salary: {self.salary}")


class Employee(Person, Company):
    def __init__(self, name, age, company_name, salary):
        Person.__init__(self, name, age)
        Company.__init__(self, company_name, salary)

    def display_all(self):
        Person.details(self)
        Company.details(self)



emp = Employee("Anita", 30, "TechCorp", 75000)
emp.display_all()
"""
#o/p--> The number of the vehicle is car
#            The engine of the bike is thar
#            The number of the vehicle is MH 35 T 4560
#            The engine of the bike is Special
#            Name: Anita, Age: 30
#            Company: TechCorp, Salary: 75000
        
#Hierarchical inheritance-->
"""

class Company:

    def __init__(self,name):
        self.name=name


    def show1(self):
        print(f'The name of the comapny is {self.name}')

class Employee(Company):

    def __init__(self,Ename,Eid):
        self.Ename=name
        self.Eid=id

    def show2(slef):
        print(f'The name of the employee is {self.Ename}')
        print(f'The ID of the employee is {self.Eid}')


class Managar(Employee):

    def __init__(self,Mname,Mdepartment):

        self.Mname=name
        self.Mdepartment=department
        super().show(self)

    def show3(self):
        print(f'The name of the manager is {self.Mname}')
        print(f'The department of the manager is {Mdepartment} ')

m=Managar()
m.show1("Cognizant")
m.show2("Shyam","h21")
m.show3("vijay","Finance Department")
print()

   """ 
#Objective:
#Create a simple library management system to manage books and track which books are borrowed or available in a library.

#Classes and Inheritance Structure:
#Parent Class: Book
#Child Class: BorrowedBook
#Explanation:
#Parent Class (Book):

#The Book class will represent the general attributes of a book.
#It will contain attributes such as:
#title: The title of the book
#author: The author of the book
#isbn: ISBN number for identification
#available: Boolean attribute to check if the book is available
#Methods in the Book class could include:
#get_details(): Displays the details of the book.
#mark_unavailable(): Marks the book as not available.
#mark_available(): Marks the book as available.
#Child Class (BorrowedBook):

#The BorrowedBook class inherits from the Book class.
#This class will handle information specific to books that are borrowed.
#Additional attributes can be added here such as:
#borrower_name: Name of the person who borrowed the book.
#due_date: The date when the book is due for return.
#Methods in the BorrowedBook class could include:
#borrow(): Takes borrower details and marks the book as borrowed.
#return_book(): Returns the book, marks it as available, and removes borrower details. 


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.available = True  

    def get_details(self):
        status = "Available" if self.available else "Not Available"
        print(f"Title: {self.title}, Author: {self.author}, "
              f"ISBN: {self.isbn}, Status: {status}")

    def mark_unavailable(self):
        self.available = False

    def mark_available(self):
        self.available = True


class BorrowedBook(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, author, isbn)
        self.borrower_name = None
        self.due_date = None

    def borrow(self, borrower_name, due_date):
        if self.available:
            self.borrower_name = borrower_name
            self.due_date = due_date
            self.mark_unavailable()
            print(f"'{self.title}' has been borrowed by {self.borrower_name}. "
                  f"Due date: {self.due_date}")
        else:
            print(f"'{self.title}' is currently unavailable.")

    def return_book(self):
        if not self.available:
            print(f"'{self.title}' has been returned by {self.borrower_name}.")
            self.borrower_name = None
            self.due_date = None
            self.mark_available()
        else:
            print(f"'{self.title}' was not borrowed.")

    def get_details(self):
        super().get_details()
        if not self.available:
            print(f"Borrowed by: {self.borrower_name}, Due date: {self.due_date}")

book1 = BorrowedBook("The Alchemist", "Paulo Coelho", "ISBN001")
book2 = BorrowedBook("1984", "George Orwell", "ISBN002")

print("Initial status:")
book1.get_details()
book2.get_details()

print("\nBorrowing a book:")
book1.borrow("Ravi Kumar", "2026-10-05")
book1.get_details()

print("\nTrying to borrow the same book again:")
book1.borrow()  






















