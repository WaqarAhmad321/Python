class Students:  # class name is written in pascal case convention i.e: HelloBro
    section = "SICSB-1"  # class attribute/variable/property/class instance

    def __init__(self, name):
        self.name = name
        print(f"*****Welcome to Basics Mr.{self.name}******")
    # self is used because the object instance is passed every time when it is called by it
    # method name is written in camel case convention i.e: helloBro

    def marks(self, total_marks):
        self.total_marks = total_marks
        print(f"The total marks of Mr.{self.name} are {self.total_marks}")
    # __init__ (constructor) is always automatically executed at first of the class

    @staticmethod  # * it is used when self is not required, to prevent positional arguement error
    def greet():
        print(f"Congratulations!You are passed.")


student1 = Students("Waqar Ahmad")
student1.roll_no = 169  # object instance
# if object instance(1st priority) is not present then it will be taken from class(2nd priority)
print(student1.section)
student1.total_marks = 427
if student1.total_marks >= 400:
    student1.greet()  # can also be used as Students.greet()
student1.marks(427)  # it is actually Students.marks(student1)
