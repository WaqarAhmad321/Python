# magic methods are special methods of oops
class Employee():
    company = "Google"

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def __len__(self):
        return len(self.name)
    # str method is used to make object meaningful when imported

    def __str__(self):
        return f"The name of the employee is {self.name} str"
    # repr method is used to recreate the object

    def __repr__(self):
        return f"Employee('{self.name}' repr)"
    # when call method is used then object can be used as a method for some functionality

    def __call__(self):
        print("Hy I am good.")


emp = Employee("Sam", 12)
print(emp)
print(repr(emp))
print(len(emp))
emp()
