print ("Welcome player are you ready?")

Direction = input("Do you want to go down the left path or right path")

if Direction == "Left" or Direction =="left":
    print ("You go towards the village")
elif Direction == "Right" or  Direction =="right":
    print("You go towards the lake")
    Answer = input("You have 2 choices to go down the left path or the right path of the cave choose wiseley")
    if Answer == "Left Path" or Answer == "left path" or Answer == "Left path" or Answer == "left Path":
        print("You have chosen correctly and now encounter the Warlock get ready to battle.")
    elif Answer == "Right Path" or Answer == "right path" or Answer == "Right path" or Answer == "right Path":
        print("You have chosen incorrectly you fall into a hole full of snakes and you die")
        exit()


print ("you encounter the warlock of the east and you must get ready to battle. He strikes you and initiates battle you know have enough energy for a hit choose wisely. ")
print("pick one, Body, Leg, Head")

attempts = 3


while attempts > 0:
    guess = input("please enter your guess")
    if guess == "Body":
        print("you have successfully killed the warlock well done!")


        break

    attempts -= 1
else:
    print("no attempts lefts")