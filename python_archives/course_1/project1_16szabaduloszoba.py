health = 20
damage = 1
Finish = 0
weight = 0
gaxe= 0
ckey = 0
print(f"""Damage: {damage}
Health: {health}""")
print(f"""Welcome to the escape room, there are 10 doors ahed of you.
There are 8 doors which will lead you to a clue that can be used to escape.
The other 2 doors are the door of freedom and the door of ethernal death.
Complete the clues to exit.""")
X=int(input("Which door do you want to go to? (0-9)"))
while Finish == 0 or health != 0:
    if X == 0:
        print(f"""Unfortunately a rat bit you and you lost 1 health.""")
        health -= 1
        print(f"""Damage: {damage}
Health: {health}""")
        X = int(input("Which door do you want to go to? (0-9)"))
    elif X == 1:
        print(f"""You entered the room and you found a
bronze sword. """)
        if weight <= 5:
            damage += 2
        else:
            print("You carry too much bronze sword. You"
                  "cannot pick up more of it.")
        print(f"""Damage: {damage}
Health: {health}""")
        X = int(input("Which door do you want to go to? (0-9)"))
    elif X == 2:
        print(f"""Unfortunately for you, you entered in the wrong room.
You saw your demise, Bill Gates came and killed you.
GAME OVER""")
        Finnish = 1
        health = 0
        print(f"""Damage: {damage}
Health: {health}""")
        X = 10
    elif X == 3:
        if gaxe == 0:
            print(f"""You entered this room but suddenly
a spider bit you and you lost 1 health.""")
            health -= 1
        else:
            print(f"""You killed a spider and found a 
BIGGER spider that damaged TWICE as more as first spider
would damage.""")
            health -= 2
        print(f"""Damage: {damage}
Health: {health}""")
        X = int(input("Which door do you want to go to? (0-9)"))
    elif X == 4:
        print(f"""You entered in a dark room and suddenly you spot an axe
in the floor.
+ 1 Bronze Axe
Total axes: {gaxe}""")
        gaxe += 1
        print(f"""Damage: {damage}
Health: {health}""")
        X = int(input("Which door do you want to go to? (0-9)"))
    elif X == 5:
        print(f"""You suddenly hear a voice: Who dares to disturb this place?
A wizard is standing next to you. You shall bring me 3 axes or I will execute you!
""")
        YY = str(input("Do you have the 3 axes? (yes/no)"))
        if YY == "yes":
            if gaxe >= 3:
                gaxe -= 3
                print(f"""Thank you for the axes. I shall reward you with a huge
reward.
+ 0.001 Health""")
                health += 0.001
            else:
                print("You failed me and now I will punish you!"
                      "")
                health -= 1
        else:
            print("You failed me and now I will punish you!"
                  "")
            health -= 1
        print(f"""Damage: {damage}
Health: {health}""")
        X = int(input("Which door do you want to go to? (0-9)"))
    elif X == 6:
        print(f"""You found the door of freedom, to be honest you
could've just look which room emits more light. This door can only
be opened with strength and an axe.""")
        Xz = str(input("Do you want to open it? (yes/no)"))
        if Xz == "yes":
            if ckey == 0:
                print("Unfortunately you were injured.")
                health -= 1
            else:
                print(f"""You got the key and you opened the door.
You go through the door but suddenly Mark Zuckerberg hits and stuns you.
Nobody knows what comes next...
(Btw you won)""")
        else:
            print(f"""You leave the door with sadness, you knew
this was the door of freedom but you couldn't open it.
Sadness hurt you!""")
            health -= 1
        print(f"""Damage: {damage}
Health: {health}""")
        X = int(input("Which door do you want to go to? (0-9)"))
    elif X == 7:
        print(f"""You just tought of the meaning of life.
You became sad and as we know sadness hurts. You
ran out of the room because there was nothing there.""")
        health -= 1
        print(f"""Damage: {damage}
Health: {health}""")
        X = int(input("Which door do you want to go to? (0-9)"))
    elif X == 8:
        print(f"""You walk in the room and you find a terrifying
creature.""")
        Xyy = str(input("Do you wanna fight him? (yes/no)"))
        if Xyy == "yes":
            if damage >= 5:
                print("You defeated the creature and it dropped a cyan key.")
                ckey = 1
            else:
                print("You were not strong enough to defeat this creature.")
                health -= 3
        else:
            print("You left the room...")
        print(f"""Damage: {damage}
Health: {health}""")
        X = int(input("Which door do you want to go to? (0-9)"))
    elif X == 9:
        print(f"""You walked in the room and
you saw a code. This code is '42784271'!""")
        print(f"""Damage: {damage}
Health: {health}""")
        X = int(input("Which door do you want to go to? (0-9)"))