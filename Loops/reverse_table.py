# To print the table of a number in reverse order
num = int(input("Enter a number : "))
for i in range(10, 0, -1):
    table = num * i
    print(num, "*", i, "=", table)
