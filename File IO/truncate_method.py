# truncate method is used to truncate(cut) the data of the file to specific file size in bytes
with open('File IO\\truncate_method.bin', 'w') as file:
    file.write('HelloWorld!')
    file.truncate(5)
with open('File IO\\truncate_method.bin', 'r') as file2:
    print(file2.read())
