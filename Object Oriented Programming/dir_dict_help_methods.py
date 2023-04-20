# dir method returns the methods and attributes available in a class
x = [1, 2, 3]
print(dir(x))
# dict method returns the object attributes of a class as dictionary


class Employee():
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary


emp = Employee("John", 20)
print(emp.__dict__)
# help method returns the help documentation of an object
print(help(emp))
