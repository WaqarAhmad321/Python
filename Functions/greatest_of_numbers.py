# To find the greatest of three numbers
def great(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        print(f"{num1} is the greatest number.")
    elif (num2 > num1 and num2 > num3):
        print(f"{num2} is the greatest number.")
    else:
        print(f"{num3} is the greatest number.")


num1 = int(input("Enter first number : \n"))
num2 = int(input("Enter second number : \n"))
num3 = int(input("Enter third number : \n"))
great(num1, num2, num3)
