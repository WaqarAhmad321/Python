# Input and Sum method in list
comp = int(input("Enter your marks in Computer : \n"))
phy = int(input("Enter your marks in Physics : \n"))
math = int(input("Enter your marks in Mathematics : \n"))
eng = int(input("Enter your marks in English : \n"))
urd = int(input("Enter your marks in Urdu : \n"))
pst = int(input("Enter your marks in Pakistan Studies : \n"))
list = [comp, phy, math, eng, urd, pst]
# sum method is used to sum the data of list
print("The Total marks obtained by student are :", sum(list))
