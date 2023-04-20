# decorators are used to modify the function
def greet(fx):
    def mfx(*args, **kwargs):
        print("*****Welcome to Decorators*****")
        print(f"The sum of numbers is {fx(*args, **kwargs)}")
        print("*****Thanks for using Decorators*****")
    return mfx


@greet
def add(num1, num2):
    return num1 + num2


add(1, 2)
