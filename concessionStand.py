#####we want to mimic a consession stand you would see at a movie centre


#we would use a dictionary to keep list of items and associated price. the dictionary would be called Menu

menu = {"pizza": 3.00,
        "nachos": 4.50,
        "popcorn" : 6.00,
        "fries": 2.50,
        "chips": 1.0,
        "pretzel": 3.50,
        "soda": 3.00,
        "lemonade": 4.25, }

cart = []   #creating an emty list variable called cart as a collection for ordered items
total = 0   #to keep track of the total

print(type(total))
print(type(menu.get("pizza")))


print("--------Menu List ----------")
for key, value in menu.items():
    print(f"{key:10} : ${value:.2f}") # to print out the keys and values with some format sepcifiers .2f and 10 spaces added

print("----------------------------")

while True:
    food = input("Select an Item from the Menu List (enter Q to quit)? : "). lower()
    if food.lower() == "q":
        print("-----Thanks for checking by------")
        break
    elif menu.get(food) is not None:
        print(f'{food} is available')
        cart.append(food)
   
for food in cart:
    total += menu.get(food, 0)  # when i used  total += menu.get(food), i ran into an error. unsupported operand type(s) for +=: 'int' and 'NoneType' while using dictionary value
    print(food, end=" ")
print()
print(total)

