import time
timestamp = time.strftime('Date : %d/%b/%Y \nTime : %I:%M %p')
print(timestamp)

hour = time.strftime('%I')
if (hour >= '0' and hour < '12'):
    print("Good Morning Sir!")
elif (hour >= '12' and hour < '17'):
    print("Good Afternoon Sir!")
elif (hour >= '17' and hour < '0'):
    print("Good Evening Sir!")
