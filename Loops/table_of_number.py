# To print the table of a number entered by the user
num = int(input("Enter a number : "))
for i in range(10):
    table = num * (i+1)
    print(num, "*", (i+1), "=", table)
