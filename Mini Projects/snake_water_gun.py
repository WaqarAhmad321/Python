import random
# function to get the result


def SnakeWaterGun(you, comp):
    if (you == comp):
        return 0
    if (you == 'r' and comp == 'p'):
        return -1
    elif (you == 'r' and comp == 's'):
        return 1
    if (you == 's' and comp == 'r'):
        return -1
    elif (you == 's' and comp == 'p'):
        return 1
    if (you == 'p' and comp == 'r'):
        return 1
    elif (you == 'p' and comp == 's'):
        return -1
    else:
        print("Invalid Choice! Play according to rules!")


print("******************Welcome To Snake Water Gun******************")
you = input(
    "Enter your choice \'r\' for rock, \'p\' for paper, \'s\' for scissor :\n")
if you == 'r':
    print('''Rock:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
          ''')
elif you == 'p':
    print('''Paper:
     _______
---'    ___)___
           ______)
          _______)
         _______)
---.__________)
''')
elif you == 's':
    print('''Scissor:
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
''')
number = random.randint(1, 3)
# Choice of computer
if (number == 1):
    print('''Rock:
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___) 
          ''')
    comp = 'r'
elif (number == 2):
    print('''Paper:
     _______
---'    ___)___
           ______)
          _______)
         _______)
---.__________)
''')
    comp = 'p'
else:
    print('''Scissor:
    _______
---'   ___)___
          ______)
       __________)
      (____)
---.__(___)
''')
    comp = 's'
result = SnakeWaterGun(you, comp)
if (result == 0):
    print("Game drawn!🙂")
elif (result == 1):
    print("You won!😃")
else:
    print("You lose!☹️")
print(f"You Choose {you} and computer choose {comp}.")
