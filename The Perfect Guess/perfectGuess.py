import random

rand_num = random.randint(30,60)

users_input = 0
i = 0

while users_input != rand_num:
    users_input = int(input("please enter a number in a range (30,60): "))
    i +=1
    print(i)
    if users_input > rand_num:
        print("Lower number please: ")
    elif users_input < rand_num:
        print("Higher number please: ")
    elif users_input == rand_num:
        print(f"Cogratulations, you have guessed the right number and you took {i} no of attempts.")