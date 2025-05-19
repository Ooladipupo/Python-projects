import random

def spin_row():
    symbols = ["⭐", "💎", "🍋", "🍒", "🍊", "🍉",]

    results = [random.choice(symbols) for i in range(3)]

    return results

def print_row(row):
    print()
    print("------------------------ ")
    print(" | ".join(row))    #using the .join() method to join the item of a list using a vertical par | as the seperator
    print("------------------------ ")


def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet*3
        elif row[0] == "🍉":
            return bet*4
        elif row[0] == "🍊":
            return bet*5
        elif row[0] == "⭐":
            return bet*6
        elif row[0] == "💎":
            return bet*7
        elif row[0] == "🍋":
            return bet*20
    else:
        return 0

def main():
    balance = 1000

    print()
    print("---------------------------")
    print("WELCOME TO PYTHON SLOTS")
    print("Symbols: 🍒 🍋 🍊 🍉 ⭐ 💎 ")
    print("---------------------------")
    print('\n')
    #print()


    while balance > 0:
        print()
        print(f"Current balance is : ${balance}")

        bet = input("Please enter your bet amount: ")

        if not bet.isdigit():
            print("Kindly enter your bet in digit greter than 0")
            continue  # the continue keywork skips this section so out code start from the beginning of the while loop again.

        bet = int(bet)

        if bet > balance:
            print("Insufficient Fund")
            continue
        
        if bet <= 0:
            print(f'Bet must be greater than Zero(0)')
            continue
            
        
        balance -= bet
        
        row = spin_row()  #we wanted to call the spin_row() method, so we assigned it to a veriable called row which 
                          #will be passed as a parameter to the print_row() function when called
        print("Spinning.....\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lose the game. tRY AGAIN")

        balance += payout

        play_again = input("Do you want to play again (Y/N)? ").lower()

        if play_again != "y" or play_again == 'n':
            break

    print("--------------------------------------")
    print(f'Game over, you balance is ${balance}')
    print("--------------------------------------")


        
       





if __name__ == '__main__':
    main()

    