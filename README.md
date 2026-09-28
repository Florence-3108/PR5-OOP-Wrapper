video:https://drive.google.com/file/d/1H_DeUnMePuzdcC8fGJJOrI2Njy3SWy4B/view?usp=drivesdk
Python OOP Project: Employee Management System

📌 Project Description

This project is a simple Employee Management System developed using Python Object-Oriented Programming (OOP) concepts.

It demonstrates important OOP concepts such as:

- Classes and Objects
- Inheritance
- Encapsulation
- Constructor ("__init__")
- Method Overriding
- "super()"
- Getters and Setters
- Private Attributes
- "issubclass()"
- Destructor ("__del__")

The program provides a menu-driven system to create and display details of a Person, Employee, and Manager.

---

🛠️ Technologies Used

- Programming Language: Python
- Concept: Object-Oriented Programming (OOP)

---

📂 Class Structure

The project contains three classes:

1. Person

The "Person" class is the base class.

It stores:

- Name
- Age

It contains a "display()" method to show person details.

class Person:
    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

---

2. Employee

The "Employee" class inherits from "Person".

It contains:

- Employee ID
- Salary

The Employee class uses private attributes:

self.__employee_id
self.__salary

Getter and setter methods are provided to access and modify these private attributes.

get_employee_id()
set_employee_id()
get_salary()
set_salary()

---

3. Manager

The "Manager" class inherits from "Employee".

It contains an additional:

- Department

It also overrides the "display()" method to show complete manager details.

Person
   ↓
Employee
   ↓
Manager

This demonstrates multilevel inheritance.

---

🔑 OOP Concepts Demonstrated

1. Inheritance

"Employee" inherits from "Person", and "Manager" inherits from "Employee".

class Employee(Person):

class Manager(Employee):

---

2. Encapsulation

Employee ID and salary are stored as private attributes.

self.__employee_id
self.__salary

They are accessed using getter and setter methods.

---

3. Constructor

The "__init__()" method initializes the objects.

Example:

def __init__(self, name="", age=0):
    self.name = name
    self.age = age

---

4. Method Overriding

The "Employee" and "Manager" classes redefine the "display()" method inherited from the parent class.

---

5. "super()"

The "super()" function is used to call the constructor of the parent class.

super().__init__(name, age)

---

6. Getter and Setter

Getter methods retrieve private data, while setter methods modify it.

Example:

def get_salary(self):
    return self.__salary

def set_salary(self, salary):
    self.__salary = salary

---

7. "issubclass()"

The program checks whether "Manager" is a subclass of "Employee".

issubclass(Manager, Employee)

The result is:

True

---

⚙️ Features

The program provides the following menu:

1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Create a Person

The user enters:

- Name
- Age

Create an Employee

The user enters:

- Name
- Age
- Employee ID
- Salary

Create a Manager

The user enters:

- Name
- Age
- Employee ID
- Salary
- Department

Show Details

The user can choose to display details of:

- Person
- Employee
- Manager

Exit

The program terminates when the user selects option "5".

---

▶️ How to Run

Step 1: Install Python

Make sure Python is installed on your computer.

Check the installation using:

python --version

Step 2: Save the Program

Save the Python code in a file such as:

employee_management.py

Step 3: Run the Program

Open the terminal in the project folder and run:

python employee_management.py

---

💻 Sample Output

--- Python OOP Project: Employee Management System ---

Choose an operation:
1. Create a Person
2. Create an Employee
3. Create a Manager
4. Show Details
5. Exit

Enter your choice: 3

Enter Name: Rahul
Enter Age: 30
Enter Employee ID: E101
Enter Salary: 50000
Enter Department: IT

Manager created with name: Rahul age: 30 ID: E101 and salary: $50000.0 and department: IT.

When displaying manager details:

Manager Details:
Name: Rahul
Age: 30
Employee ID: E101
Salary: $50000.0
Department: IT

---

🎯 Learning Objectives

After completing this project, you can understand:

- How to create Python classes and objects
- How inheritance works
- How multilevel inheritance works
- How encapsulation protects data
- How getters and setters are used
- How constructors work
- How method overriding works
- How "super()" is used
- How "issubclass()" checks inheritance relationships
- How to create a menu-driven Python application

---

📁 Project Structure

Employee-Management-System/
│
├── employee_management.py
└── README.md

---

👨‍💻 Conclusion

The Employee Management System is a beginner-friendly Python OOP project that demonstrates multiple Object-Oriented Programming concepts through a simple menu-driven application.

It provides practical understanding of inheritance, encapsulation, constructors, method overriding, getters, setters, and class relationships.
