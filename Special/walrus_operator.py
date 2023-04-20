# walrus operator is used to assign value to a variable within an expression
while (number := int(input("Enter a number :"))) != 0:
    if number == 0:
        print("Equal to zero.")
    elif number > 0:
        print("Greater than zero.")
    else:
        print("less than zero.")
