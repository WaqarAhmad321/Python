# if a child class have more than one parents multiple inheritance

class Student():
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def showDetails(self):
        print(f"The name and rollno of Student are {self.name} {self.rollno} ")


class Talent():
    def __init__(self, talent):
        self.talent = talent

    def showDetails(self):
        print(f"The talent of the Student are {self.talent}")


class Info(Student, Talent):
    def __init__(self, name, rollno, talent):
        # super().__init__(name, rollno, talent)
        self.name = name
        self.rollno = rollno
        self.talent = talent


infor = Info("Waqar", 169, "Computers")
infor.showDetails()
# * method resolution order (which class method will be priortized)
print(Info.mro())
