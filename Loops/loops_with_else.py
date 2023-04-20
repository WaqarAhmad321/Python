# else is executed only when the loop is successfully completed , it's execution means loop is successfull completed
for i in range(6):
    print(i)
    if (i == 4):
        break
else:
    print("The loop is successfully ended not breaked.")
