num = int(input("Enter a number between 5 and 7 :\n"))
char = str(num)
if (num < 5 or num > 9):
    raise ValueError("Value Error!")
elif char == "quit":
    print("Done!")
