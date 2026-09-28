class Person:               

    def __init__(self, name="", age=0):
        self.name = name
        self.age = age

    def display(self):
        print("\nPerson Details:")
        print("Name:", self.name)
        print("Age:", self.age)

    def __del__(self):
        pass

class Employee(Person):

    def __init__(self, name="", age=0, employee_id="", salary=0):
        super().__init__(name, age)

        self.__employee_id = employee_id
        self.__salary = salary

    def get_employee_id(self):
        return self.__employee_id

    def set_employee_id(self, employee_id):
        self.__employee_id = employee_id

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def display(self):
        print("\nEmployee Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.__employee_id)
        print("Salary: $", self.__salary, sep="")

    def __del__(self):
        pass

class Manager(Employee):

    def __init__(self, name="", age=0, employee_id="", salary=0, department=""):
        super().__init__(name, age, employee_id, salary)
        self.department = department

    def display(self):
        print("\nManager Details:")
        print("Name:", self.name)
        print("Age:", self.age)
        print("Employee ID:", self.get_employee_id())
        print("Salary: $", self.get_salary(), sep="")
        print("Department:", self.department)

    def __del__(self):
        pass

person = None
employee = None
manager = None

print("\n--- Python OOP Project: Employee Management System ---")

while True:

    print("\nChoose an operation:")
    print("1. Create a Person")
    print("2. Create an Employee")
    print("3. Create a Manager")
    print("4. Show Details")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))

        person = Person(name, age)

        print(f"\nPerson created with name: {name} and age: {age}.")

    elif choice == 2:

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))

        employee = Employee(name, age, employee_id, salary)

        print(f"\nEmployee created with name: {name} age: {age} ID: {employee_id} and salary: ${salary}.")

    elif choice == 3:

        name = input("\nEnter Name: ")
        age = int(input("Enter Age: "))
        employee_id = input("Enter Employee ID: ")
        salary = float(input("Enter Salary: "))
        department = input("Enter Department: ")

        manager = Manager(name, age, employee_id, salary, department)

        print(f"\nManager created with name: {name} age: {age} ID: {employee_id} and salary: ${salary} and department: {department}.")

    elif choice == 4:

        print("\nChoose details to show:")
        print("1. Person")
        print("2. Employee")
        print("3. Manager")

        detail_choice = int(input("\nEnter your choice: "))

        if detail_choice == 1:

            if person is not None:
                person.display()
            else:
                print("\nNo Person has been created.")

        elif detail_choice == 2:

            if employee is not None:
                employee.display()
            else:
                print("\nNo Employee has been created.")

        elif detail_choice == 3:

            print("Is Manager a subclass of Employee?\n", issubclass(Manager, Employee))

            if manager is not None:
                manager.display()
            else:
                print("\nNo Manager has been created.")

        else:
            print("\nInvalid choice.")

    elif choice == 5:

        print("\nExiting the system. All resources have been freed.")
        print("\nGoodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")