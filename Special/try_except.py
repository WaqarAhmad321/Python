num = input("Enter a number :\n")
try:
    for i in range(1, 11):
        print(f"{int(num)} X {i} = {int(num) * i}")
except:
    print("Invalid Input")
