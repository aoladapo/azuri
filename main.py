import random

play_on = True
while play_on:
    options = {"R": "Rock", "P":"Paper", "S":"Scissors"}
    opt = ["R", "P", "S"]
    player = input("Choose R(Rock), P(Paper) or S(Scissors): ").upper()
    computer = random.choice(opt).upper()
    print(f"player'({player})':computer'({computer})'")
    if player not in opt:
        print('Error !!!, invalid input')
        continue
    if player == computer:
        print('That is a draw')
    if player == "R" and computer == "S":
        print("You win")
    else:
        if player == "S" and computer == "R":
            print("You lost")
    if player == "P" and computer == "R":
        print("You win")
    else:
        if player == "R" and computer == "P":
            print("You lost")
    if player == "S" and computer == "P":
        print("You win")
    else:
        if player == "P" and computer == "S":
            print("You lost")