import random
print('''
 ,adPPYb,d8 88       88  ,adPPYba, ,adPPYba, ,adPPYba,  
a8"    `Y88 88       88 a8P_____88 I8[    "" I8[    ""  
8b       88 88       88 8PP"""""""  `"Y8ba,   `"Y8ba,   
"8a,   ,d88 "8a,   ,a88 "8b,   ,aa aa    ]8I aa    ]8I  
 `"YbbdP"Y8  `"YbbdP'Y8  `"Ybbd8"' `"YbbdP"' `"YbbdP"'  
 aa,    ,88                                             
  "Y8bbdP"                                              
      ''')
print("***************Welcome to Number Guessing game***************")
num = random.randint(1, 100)
guess = None
nguess = 1
while (guess != num):
    guess = int(input(("Guess a number between 1 and 100 : \n")))
    if (guess > num):
        print("Lower number please!")
    elif (guess < num):
        print("Higher number please!")
    nguess = nguess + 1
print(f"You guessed it in {nguess} attempts.")
