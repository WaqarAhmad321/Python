# To change the data of a tuple by converting it into list
tup = ("Waqar", "Ahmad", 3, 2, 1, "Go")
temp = list(tup)
temp.append("!")
tup = tuple(temp)
print(tup)
