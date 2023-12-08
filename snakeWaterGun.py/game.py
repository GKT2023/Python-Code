import random

def gameWinner(machine_turn, yourTurn):
    if yourTurn == machine_turn:
        return None

    if machine_turn == 's':
        if yourTurn == 'w':
            return False
        elif yourTurn == 'g':
            return True
    elif machine_turn == 'w':
        if yourTurn == 's':
            return True
        elif yourTurn =='g':
            return False
    elif machine_turn == 'g':
        if yourTurn == 's':
            return False
        elif yourTurn == 'w':
            return True
    
    
print("Machine turn: choose among snake(s), water (w) and gun(g)")
random_no = random.randint(1,3)

if random_no == 1:
    machine_turn = 's'
elif random_no == 2:
    machine_turn = 'w'
elif random_no == 3:
    machine_turn = 'g'
yourTurn = input("My turn: choose among snake(s), water (w) and gun(g): ")

out = gameWinner(machine_turn, yourTurn)

if out == None:
    print("it was a tie")
elif out == True:
    print("YOu win!")
else:
    print("You Loose.")
