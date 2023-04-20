# To print the sum of n natural numbers
def sum(n):
    if (n == 0):
        return 0
    elif (n == 1):
        return 1
    else:
        return sum(n - 1) + n


n = int(input("Enter a number : \n"))
print("The sum of numbers is :", sum(n))
