print("**********Welcome to the tip calculator**********")
bill = float(input("What was the total bill? $"))
percentage = int(
    input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
tip = ((((percentage / 100) * bill) + bill) / people)
print(f"Each person should pay: ${round(tip, 2)}")
