from math import sqrt


class Calculator:
    def __init__(self, number):
        self.number = number

    def square(self):
        print(f"The square of {self.number} is {self.number **2}")

    def sqrt(self):
        print(f"The square root of {self.number} is {sqrt(self.number)}")

    def cube(self):
        print(f"The square root of {self.number} is {self.number ** 3}")


number = int(input("Enter a number :\n"))
num = Calculator(number)
num.square()
num.sqrt()
num.cube()
