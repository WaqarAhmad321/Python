# seek method is used to move the current position to specified position in bytes in the file
with open('File IO\\seek_method.txt', 'r') as file:
    file.seek(10)
    data = file.read(5)
    print(data)
