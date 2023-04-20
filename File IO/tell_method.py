# tell method is used to check specified position in bytes in the file
with open('File IO\\tell_method.txt', 'r') as file:
    file.seek(10)
    tells = file.tell()
    data = file.read(5)
    print(data)
    print(tells)
