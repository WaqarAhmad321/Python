print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
      ''')
print("***********Welcome to Your Calculator***************")
try:
    n1 = int(input("Enter first number : "))
except ValueError:
    print("Invalid Value! Restart the program for correct answers.")
opp = input("Enter the operation (+, -, *, /, %, **) : ")
try:
    n2 = int(input("Enter second number : "))
except ValueError:
    print("Invalid Value! Restart the program for correct answers.")
if opp == '+':
    add = n1 + n2
    print(f"Addition of {n1} and {n2} is {add}")
    print("-----------Cool-----------")
elif opp == '-':
    sub = n1 - n2
    print(f"Substraction of {n1} and {n2} is {sub}")
    print("-----------Cool-----------")
elif opp == '*':
    mul = n1 * n2
    print(f"Multiplication of {n1} and {n2} is {mul}")
    print("-----------Cool-----------")
elif opp == '/':
    div = n1 / n2
    print(f"Division of {n1} and {n2} is {div}")
    print("-----------Cool-----------")
elif opp == '%':
    mod = n1 % n2
    print(f"Modulus of {n1} and {n2} is {mod}")
    print("-----------Cool-----------")
elif opp == '**':
    expo = n1 ** n2
    print(f"Exponential of {n1} w.r.t {n2} is {expo}")
    print("-----------Cool-----------")
elif opp == '//':
    flo = n1 // n2
    print(f"Float of {n1} and {n2} is {flo}")
    print("-----------Cool-----------")
else:
    print("Invalid Operation!")
print("*********Thank You ! For using this calculator********")
