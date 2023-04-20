# super keyword is used to access all the methods and attributes of a parent class by a child class

class Group():
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno

    def parentClass(self):
        print("This is a parent method.")


class Students(Group):
    def __init__(self, name, rollno, lang):
        super().__init__(name, rollno)
        self.lang = lang

    def childClass(self):
        # child class attribute will be priotized
        print(f"This is a child class. parent class group is {self.name}")
        super().parentClass()


g = Group("Waqar", 169)
s = Students("Ammar", 12, "German")
s.childClass()
# print(s.overrided())
