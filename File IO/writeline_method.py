# write line method is used to write strings in a file
file = open("File IO\writeline_methd.txt", "w")
list = ["hello!\n", "There\n", "Bye\n"]
file.writelines(list)
