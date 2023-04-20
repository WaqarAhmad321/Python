intro = "Hi! My name is {1} and I am from {0}"
name = ["Waqar", "Pakistan"]
print(intro.format(name[0], name[1]))
print(f"Hi! My name is {name[0]} and I am from {name[1]}")
print(f"Hi! My name is {{name[0]}} and I am from {{name[1]}}")
