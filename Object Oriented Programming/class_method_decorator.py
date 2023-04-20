# class method decorator is used to change the value class variable
class Employee:
    company = "Google"

    def __init__(self, name, company):
        self.name = name
        self.company = company

    def showDetails(self):
        print(
            f"The name of employee is {self.name} and company is {self.company}")

    @classmethod  # in it the first argument is given as a class not as an object so that it can change the class variable
    def changeCompany(cls, newcompany):
        cls.company = newcompany


emp1 = Employee("Ali", "Apple")
emp1.showDetails()
print(Employee.company)
Employee.changeCompany("Amazon")
print(Employee.company)
