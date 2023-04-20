# readline method is used to read lines from a file
file = open('File IO\\readline_method.txt', 'r')
i = 1
while True:
    lines = file.readline()
    if not lines:
        break
    m1 = lines.split(",")[0]
    m2 = lines.split(",")[1]
    m3 = lines.split(",")[2]
    print(f"Marks of student {i} are {m1}, {m2}, {m3}")
    i += 1
file.close()
