import random


def gameWin(Computer, you):
    if Computer == you:
        return None
    elif Computer == 's':
        if you == 'w':
            return False
        elif you == 'g':
            return True
    elif Computer == 'w':
        if you == 's':
            return True
        elif you == 'g':
            return False
    elif Computer == 'g':
        if you == 's':
            return False
        elif you == 'w':
            return True


print("Computer Turn: Snake(s) Water(w) or Gun(g)?")
randNo = random.randint(1, 3)

if randNo == 1:
    Computer = 's'
elif randNo == 2:
    Computer = 'w'
elif randNo == 3:
    Computer = 'g'

you = input("Your Turn: Snake(s) Water(w) or Gun(g)?")
a = gameWin(Computer, you)

print(f"computer chose {Computer}")
print(f"You chose {you}")
if a == None:
    print("The game is a tie!")
elif a:
    print("you Win!")
else:
    print("you Lose!")
