print('''   
                        88            
                        ""            
                                      
 ,adPPYb,d8 88       88 88 888888888  
a8"    `Y88 88       88 88      a8P"  
8b       88 88       88 88   ,d8P'    
"8a    ,d88 "8a,   ,a88 88 ,d8"       
 `"YbbdP'88  `"YbbdP'Y8 88 888888888  
         88                           
         88                           
      ''')
print("***************Welcome to Quiz Compitetion***************")
queslist = ["When Pakistan became an independent country (year) : ",
            "When bangladesh separated from Pakistan : ", "How many provinces of Pakistan: ",
            "In which year did Pakistan win the Cricket World Cup : ", "When did Pakistan win Olympic gold medal in Hockey for the first time"]
anslist = ["1947", "1971", "4", "1992", "1960"]
score = 0
# q no 1
print(f"Q no 1. {queslist[0]}")
ans1 = input()
if (ans1 == anslist[0]):
    print("Your answer is Correct")
    score = score + 1
else:
    print("Your answer is Incorrect")
# q no 2
print(f"Q no 2. {queslist[1]}")
ans1 = input()
if (ans1 == anslist[1]):
    print("Your answer is Correct")
    score = score + 1
else:
    print("Your answer is Incorrect")
# q no 3
print(f"Q no 3. {queslist[2]}")
ans1 = input()
if (ans1 == anslist[2]):
    print("Your answer is Correct")
    score = score + 1
else:
    print("Your InYour answer is Incorrect")
# q no 4
print(f"Q no 4. {queslist[3]}")
ans1 = input()
if (ans1 == anslist[3]):
    print("Your answer is Correct")
    score = score + 1
else:
    print("Your answer is Incorrect")
 # q no 5
print(f"Q no 5. {queslist[4]}")
ans1 = input()
if (ans1 == anslist[4]):
    print("Your answer is Correct")
    score = score + 1
else:
    print("Your answer is Incorrect")
print("***************Thanks ! Your result is given below :-)***************")
print(f"Your scored {score} out 5")
