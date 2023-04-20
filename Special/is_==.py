# 'is' compares the exact location of the object(variable)
# '==' compares the value of the object
# a = 3  a and b will point to 3 to save memory
# b = 3
# print(a is b)
# print(a == b)
a = (1, 2, 3)
b = (1, 2, 3)
print(a is b)
print(a == b)
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # because list is mutable so stored at different locations
print(a == b)
