import random


words = ("apple", "orange", "banana", "coconut", "pineaple")



# lets add a dictionary of key: (). meaning keys and turple. each turple consisting of three strings
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" o ",
                   "   ",
                   "   "),
               2: (" o ",
                   " | ",
                   "   "),
               3: (" o ",
                   "/| ",
                   "   "),
               4: (" o ",
                   "/|\\",
                   "   "),
               5: (" o ",
                   "/|\\",
                   "/  "),
               6: (" o ",
                   "/|\\",
                   "/ \\"),}

#print(hangman_art[0])



def display_man(wrong_guesses):
    print("****************")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("****************")


def display_hint(hint):
    print(" ".join(hint)) #string has a builtin .join() method which can be used to join a string together with a delimeter included within " " if necessary


def display_answer(answer):
    print(" ".join(answer))
    print(answer)


def main():
    answer = random.choice(words)
    hint = ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set() #the set function set() is used to create empty set in python because its impossible to create an empty set with just paranthesis ()
    is_running = True  #a boolean to be used for our while statement to run while True untill when False to exit the game


    while is_running:
        display_man(wrong_guesses)              #we called the first function we defined above
        display_hint(hint)
        display_answer(answer)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or guess.isdigit():                     #input validation to make sure only one letter is added at a time. if input is invalid, we continue to skip so user can add the right input
            print("Invalid Input Guess only a Letter")
            continue

        

        if guess in guessed_letters:
            print(f'{guess} is already guessed')
            continue

        guessed_letters.add(guess)


        if guess in answer:                     #using the in as a membership operator
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1


        if "_" not in hint:
            display_man(wrong_guesses)
            display_answer(answer)
            print("YOU WIN")
            is_running = False
        elif wrong_guesses >= len(hangman_art) - 1:
            display_man(wrong_guesses)
            display_answer(answer)
            print("You LOSE")
            is_running = False

if __name__ == '__main__':
    main()
