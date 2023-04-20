# To check whether the person is teenage, child or an adult
age = int(input("Enter your age : "))
if (age < 15 and age > 1):
    print("Your are a child.")
elif (age >= 15):
    if (age >= 15 and age < 17):
        print("You are a teenager.")
    else:
        print("You are an adult.")
else:
    print("Your are not born yet!")
