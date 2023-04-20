# copy method is used to copy the content of a list into another variable
def function(a, b):
    return a + b


l = ["Hello", "Hello", 2]
c = l.copy()
c[0] = 0
print(c)
print(function(1, 2))
