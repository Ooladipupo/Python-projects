import random
lowest_num = 1
highest_num = 100


answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True # we would set is_running to start our while loop of the guess game. 
                    #once guessed number equal the random number, we would set is_running to false to terminate the loop and game

print("Python number guess game")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:

    guess = input(f"Enter your guess Here between {lowest_num} and {highest_num}: ")

    if guess.isalpha():
        print(f"iNVALID GUESS, please enter your guess again between {lowest_num} and {highest_num}: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        

        if guess > highest_num:
            print("guess is outside range")
            print(f"Please select the number between {lowest_num} and {highest_num}: ")
        elif guess > answer:
            print("Too High. Try Again")
        elif guess < answer:
            print("Too Low. Try Again")

        else:
            print(f"correct. the answer is {guess}Start a new game")
            print(f'Number of gusses is {guesses}')
            is_running = False

print(answer)
