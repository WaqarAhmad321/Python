# To print the table of a number
def table(n):
    for i in range(1, 11):
        print(f"{n} * {i} = ", n * i)


n = int(input("Enter a number : "))
table(n)
