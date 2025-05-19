def show_balance():
    
    print("Tranaction processing")
    print(f"Your balance is ${balance:.2f}")
    return f'Transaction complete'

def deposit():
    deposite_amount = float(input("Enter an amount to be deposited: "))
    if deposite_amount < 0:
        print("Youve entered an invalid amount")
        return 0
    else:
        return deposite_amount


def withdraw():
    withdraw_amount = float(input("Enter amount to withdrawl: "))
    if withdraw_amount < 0:
        print("amount must be greater than zero")
        return 0
    elif withdraw_amount > balance:
        print("Insufficient Account Balance")
        return 0
    else:
        return withdraw_amount

balance = 3
is_running = True


while is_running:
    print()
    print("----Banking programe---")
    print("1 - Show Balance")
    print("2 - Make Deposite")
    print("3 - Withdraw")
    print("4 - Exit")
    print("----------------------")
    print()

    choice = int(input("Enter your BANKING choice (1 - 4): "))

    if choice == 1:   #if a user enter option 1, we should call the show_balance function
        print(show_balance())

    elif choice == 2:   #if a user enter option 2, we should call the deposite function
        balance += deposit()
        print(f'Your new balance is {balance}')
        

    elif choice == 3:   #if a user enter option 3, we should call the withdraw function
        balance -= withdraw()
        print(f'Your new balance is {balance}')
    
    elif choice == 4:   #if a user enter option 4, we should exit the progrme by making the while loop false
        is_running = False

    else:
        print("Invalid CODE")
        choice = int(input("Enter your BANKING choice (1 - 4): "))
        #is_running = False
print("Thank you! Have a Nice Day")
print(balance)
    
