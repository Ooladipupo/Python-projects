import random
options = ("rock", "paper", "scissors")

running = True

while running:

    player = None
    computer = random.choice(options) #using the choice() method to pick a random coice from the option turple



    while player not in options:

        player = input(f"Enter your choice from this item {options}: ")


    if player == computer:
        print("a tie")
    elif player == "rock" and computer =="scissors":
        print("You are the Winner!")
    elif player == "paper" and computer =="rock":
        print("You are the Winner!")
    else:
        print("YOU LOSE, End of Game")
        running = False

    print(f'Player: {player}')
    print(f'computer: {computer}')

