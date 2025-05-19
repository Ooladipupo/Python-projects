import random


print("\u250CF \u250C \u2500 \u2502 \u2514 \u2518 \u2513 \u2510") #lets enter some unicode character to create out ASCII character ● ┌ ─ │ └ ┘

# ┌ F  ─ │ └ ┘ ┓ ┐  WE WOuld use theis character to make our die using about 5 characters per die

#lets create a basic box shape first
"""
"┌─────────┐"
"│         │"
"│    ●    │"
"│         │"
"└─────────┘"
"""

#lets crate a dictionary of a turple key value pair

dice_art = {1:("┌─────────┐"
               "│         │"
               "│    ●    │"
               "│         │"
               "└─────────┘"),
            2:("┌─────────┐"
               "│ ●       │"
               "│         │"
               "│       ● │"
               "└─────────┘"),
            3:("┌─────────┐"
               "│ ●       │"
               "│    ●    │"
               "│       ● │"
               "└─────────┘"),
            4:("┌─────────┐"
               "│ ●     ● │"
               "│         │"
               "│ ●     ● │"
               "└─────────┘"),
            5:("┌─────────┐"
               "│ ●     ● │"
               "│    ●    │"
               "│ ●     ● │"
               "└─────────┘"),
            6:("┌─────────┐"
               "│ ●     ● │"
               "│ ●     ● │"
               "│ ●     ● │"
               "└─────────┘"),
            }

dice = []
total = 0
number_of_dice = int(input("How many dice ?: "))


for die in range(number_of_dice):
    dice.append(random.randint(1, 6))


for die in range(number_of_dice):
    for line in dice_art.get(dice[die]):
        print(line, end="")
    print()

for die in dice:
    total += die
print(f' our total {total}')




