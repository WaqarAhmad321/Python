class Employee():
    company = "Google"
    language = "Go"

    def showDetails(self):
        print(f"{self.company}")


class Programmer(Employee):
    company = "Youtube"
    language = "Python"

    def shoDetails(self):
        print(f"{self.company}")


emp = Employee()
emp.showDetails()
pro = Programmer()
pro.showDetails()
