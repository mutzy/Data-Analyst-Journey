# Python classes Tutorial

## Introduction

Python is an object oriented programming language, with almost everything is an object, with its properties and methods.
A Class is like an object constructor, or a "blueprint" for creating objects.

## Goal

Data Processing Script
This script processes input data, performs analysis, and outputs results.

## Let's Start

### Classes

We will start of my creating a class and understanding the difference between a class and a function in python.

Classes as defined above act like object, and Object is basically something that has a key and a value. eg:

````
```Objectvar = {
 'name': "mutuku",
 'age':30
}```
````

The above can then be accessed as shown below:

````
 ```Objectvar.name```
````

The result from the above should be:

````
 ```"mutuku"```
````

Classes unlike functions start with the keyword "class". eg:

````
 ``` class ClassName():```
````

while as we saw in our last session functions start with the keyword "def". eg:

````
 ```def FunctionName():```

````

### Okay Shift Gears

#### Example class in python

```
class Student():
   def __init__(self, name,gender):
    self.studentname = name
    self.gender = gender

   def __str__(self):
    return f"Hello {self.studentname} welcome to the {gender(self.gender) } domitories"

   def gender(gender):
     roomtype = "Boy's"
     if(gender != "male"){
      roomtype = "Girl's"
     }

```

The above is an example to how a basic class layout looks like in python, so lets understand it better.
class and class name is what starts, always remember indentation when movin to newlines. The **init**() in a python built in function allows you to initiate parameters and is always first to be executed in any python class.

The **str**() is also a built in python function that allows you to output information in string format as you can see above.

The gender() function is my own function you can add as many as needed this allows us to check the gender of the student and correctly display the word that will make sense.

Let us execute the above code:

```
student = Student('Carol', 'female')
print(student)

OUTPUT:
Hello Carol welcome to the girl's domitories.

```

### Assignment: Building a Library Management System

#### Objective:

Create a Python program to manage a small library system using classes. The system should be able to handle books and members, allowing members to borrow and return books.

#### Requirements:

    - Book Class:
        - Attributes:
            * title (str)
            * author (str)
            * isbn (str)
            * available (bool) - default should be True
        - Methods:
            * __str__: Returns a string representation of the book.

    - Member Class:
        - Attributes:
            * name (str)
            * member_id (str)
            * borrowed_books (list) - stores the books borrowed by the member
        - Methods:
            * borrow_book(book): Allows the member to borrow a book if it is available.
            * return_book(book): Allows the member to return a borrowed book.
            * __str__: Returns a string representation of the member.

    - Library Class:
        - Attributes:
            * books (list) - stores all books in the library
            * members (list) - stores all members of the library
        - Methods:
            * add_book(book): Adds a book to the library.
            * remove_book(book): Removes a book from the library.
            * register_member(member): Registers a new member to the library.
            * deregister_member(member): Deregisters a member from the library.
            * list_available_books(): Lists all available books in the library.
            * __str__: Returns a string representation of the library.

#### Instructions:

    - Define the Book class with the specified attributes and methods.
    - Define the Member class with the specified attributes and methods.
    - Define the Library class with the specified attributes and methods.
    - Demonstrate the functionality by:
        * Creating instances of Book and Member.
        * Adding books to the library.
        * Registering members to the library.
        * Borrowing and returning books.
        * Listing available books.

### How to test your work

### Create some book instances

```
book1 = Book(title="1984", author="George Orwell", isbn="1234567890")
book2 = Book(title="To Kill a Mockingbird", author="Harper Lee", isbn="0987654321")
```

### Create a member instance

```
member1 = Member(name="John Doe", member_id="001")
```

### Create a library instance

```
library = Library()
```

### Add books to the library

```
library.add_book(book1)
library.add_book(book2)
```

### Register member to the library

```
library.register_member(member1)
```

### Member borrows a book

```
member1.borrow_book(book1)
```

### List available books

```
print(library.list_available_books())
```

### Member returns a book

```
member1.return_book(book1)
```

### List available books

```
print(library.list_available_books())
```

## Github

Push you work to "python-classes" branch
