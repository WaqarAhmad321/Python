print("*************************Welcome to Treasure Island*************************")
print('''
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
''')
print('''You are a treasure hunter who has received a tip about a hidden treasure on a distant island. As you approach the island, you see that there are two paths leading inland. One path is overgrown and looks like it hasn't been used in years, while the other path is well-trodden and leads towards a clearing.What will you do?
a. Take the overgrown path
b. Take the well-trodden path
''')
first_choice = input("Choose \'a\' or \'b\' : ").lower()
if first_choice == 'a':
    print('''As you make your way through the dense vegetation, you come across a small pond. You decide to take a break and refill your canteen, when suddenly you see something glinting at the bottom of the pond. Excited, you dive in and retrieve a small chest filled with gold coins. You open the chest and find a map inside, leading to the location of the main treasure. What will do?
    a. Follow the map to the main treasure
    b. Take the gold coins and return to civilization''')
    second_choice = input("Choose \'a\' or \'b\' : ").lower()
    if (second_choice == 'a'):
        print('''You follow the map to the main treasure and find a large chest filled with gold and jewels. You take as much as you can carry and make your way back to your boat, feeling exhilarated by your success.''')
    else:
        print('''You decide that the gold coins are enough and return to civilization, where you sell them and live the rest of your life in luxury.''')
else:
    print('''You follow the well-trodden path and eventually come to a clearing where you see a group of bandits. They demand that you hand over all of your valuables. Do you:
    a. Hand over your valuables
    b. Try to fight the bandits''')
    third_choice = input("Choose \'a\' or \'b\' : ").lower()
    if (third_choice == 'a'):
        print('''The bandits take your valuables and let you go, warning you not to try to retrieve them. Disheartened, you return to your boat and head back to civilization.''')
    else:
        print('''You manage to defeat the bandits and continue your search for the treasure. After several more hours of searching, you come across a hidden cave and find the treasure you have been searching for. You take as much as you can carry and make your way back to your boat, feeling exhilarated by your success.''')
