"""
import sys

print(sys.version)

if 5 > 2:
    print("five is greater than 2")

if 5 > 2:
    print("five is less thghhhhhhhhan 2")

x = int(3)

print(type(x))

fruit = ["orange", "book", "tail"]
x,y,z = fruit

print(x)
print(y)
print(z)

x ="fantastic"

def olafunc():
    global x
    x = "babababna"
    print("my name is", x)

olafunc()

print("my name is", x)

x = y = z = "hello"

print(x)

for x in "banana":
    print(x)

for x in range(1,10):
    print(x)



email = "bolekaja@gmail.com"
print("i like pizza, kindly send the invoice to my {email} address")


# tring if statement
ola_student = False

if ola_student:
    print("you are a student")
else:
    print("you are not a student")


age = ""
#age = str(age)

#age += '2'   #using a methematical expression here on string. This is not really applicable in most uses cases

print(age)
print(bool(age))


#input

x = input("what is your name? ")
a = int(input("what is your mother age"))

#a = int(a)

a += 2

print(f'my name is {x}, and i am {a} old')

""

#Madlibs game

adjective1 = str(input("enter an adjective (description):"))
noun = input("Enter a noun (person, place, or thing):")
adjective2 = input("Enter an adjective ()description:")
verb1 = input("enter a verb ending with 'ing'")
adjective3 = input("Enter an adjective (description):")

print(f"Today i went to a {adjective1} zoo.")
print(f"In an exhibit, i saw a {noun}")
print(f"{noun} was {adjective2} and {verb1}")
print(f"i was {adjective3}")

""

#lets calculate the area of a circle Pie r power 2. we need the Math Library

import math

radius = float(input("Enter the radius of a circle here: "))

#area = math.pi * radius**3
area = math.pi * pow(radius, 2)         #same as above line. we usd the pow() method here

print(round(area))     #round up answer to the nearest number using the round() method

""

#print the squarroot of the sum of a2 and b2 quare. 

import math

a = float(input("Enter side A: "))
b = float(input("Enter side B"))

a **= 2
b **= 2

c = a + b

print(math.sqrt(c))
""

#leaning If ststement

age = int(input("Enter your age here:  "))

if age > 18:
    print(f"Your are allowed to continue since you are greater than {age}")

elif age == 18:
    print(f' we will gar back to you cos you just clockd {age}')

elif age ==" ":
    print("you are yet to type your age. start again")

else: 
    print(f' Try again when you clock {age}')
""

name = input("please enter your name here:  ")

if name == "":
    print("you need to enter your name please")

else:
    print(f"my name is {name}")

""
#lets code a weight conversion application

weight =float(input("Enter your body weight"))

unit = input("Enter your unit of measurement (k for Kilograms or P for Pounds)")

if unit == "K":
    result = str(weight) + " " + "Kg"
    print(round(result))

elif unit == "P":
    result = round(weight*2.20580, 1)
    print(f'your body is weigh {result} Lbs')

else:
    print(f"kindly enter only a valid input (P or K)")
""

#we can also code a temperture conversion application following the above illustration.


#lets do something else with OR |, AND &, NOT logical conditions.

temp = int(input("kindly enter todays temperature"))

is_raining = True

if temp > 35 and not is_raining:
    print("todays event is cancelled")
else:
    print("we are procedding with todays events")
""


#learning CONDITIONal EXPRESSION - a one line if else condition statement
#thr format is 'return x if condition is true, else y

num = int(input("enter an interger"))

result = "even" if num%2 == 0 else "negtive"
print(result)

""


#string manipulation like spliting, etc

a = "ola olufowobi yusuf"

print(len(a))

result = a.rfind("z")
print(result)

re = a.isdigit()
print(re)

print(help(str))
""


#write a code to implement password policy

username = input("Enter a new user name here : ")

if not 15 > len(username) > 8:          #only password length between 8 to 15 chnaracter accepted
    print("kindly enter a password between 8 to 15 character")
elif not username.find(" ") == -1:          #useing the finc("") method to be sure no space is created in the usename
    print("username should not contain space")
elif not username.isalpha():                #using the alpha() method to eb sure only alphabets are allowed in the usename
    print("only aphabets are alled in a username")


else:
    print(username)
    print("your username didnt contain space as required")


""

#Lets learn WHILE loop
#WHILE a condition is true, continue to execute the code

#name = input("enter your name here : ")

#while name == "":
#    print("you didnt enter your name")
#    name = input("enter your name again")   #to prevent infinif looping when a while loop executed, we smartly include an INPUT demand to excape contious looping

#print(f'Hello {name} welcome to the club')  #this line execute when out WHILE condition is False

#lets try another example with age

#age = int(input("please enter your age"))

#while age < 0:
#    print("age cant be negative")
 #   age = int(input("please input your age"))
#
#print(f' your age is {age} years ols')


user_name = "olad"
password = input("kindly enter your password")

while user_name == "olad" and password != "baba2234":
    print("youve entered a wrong password")
    password =input("key in your password again")

print(f'welcome {user_name}')

""

#lets calculate compound interest

principle = 0
rate = 0
time = 0

while principle <= 0:
    principle =float(input("enter the principla amount "))
    if principle <= 0:
        print("principle cant be less than or equal zero")

while rate <= 0:
    rate =float(input("enter the interest rate "))
    if rate <= 0:
        print("rate cant be less than or equal zero")

while time <= 0:
    time =float(input("enter the time in years "))
    #if time <= 0:
    print("time cant be less than or equal zero")

print(principle)
print(time)
print(time)

total = principle * pow((1 + rate / 100), time)
print(f'${total:,.2f}')

"""

#For loop

#for i in range(20, 1, -1):
#    print(i, end=" -")

#print("i am a boy")


#nested Loop
"""
for x in range(3):
    for i in range(20, 1, -1):
        print(i, end=" -")
    print()

""
#this cod print out a rectangle of $ that has 4 roles and 10 coulmns
row = int(input("enter the number of rows:"))
column = int(input("enter the number of column:"))
symbol = (input("enter a symbol here:"))

for i in range(row):
    for x in range(column):
        print(symbol, end="")
    print()
"""

#Collections in python include list[], set{} and Turple()

#fruits = {"apply", "orange", "banana", "coconut", "apply"}

#fruits.add("orange")

#print(fruits)

#fruits.pop()
#print(fruits)

"""

##lets build a shopping cart programe

foods = []
prices = []
total =0

while True:
    food = input("Enter a food to buy (q to quit)")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter price of {food} here in dollars: $"))
        print(f'my food is {food}, and it cost : &{price:.2f}')

        foods.append(food)
        prices.append(price)


    print(foods)
    if len(foods) > 4:
        print("you are only permitted to select 4 foods")
        break
    print(prices)

    ""


# 2 D Dimention. THis is a collection of list within list

fruits =    ["apple", "orange", "banana", "coconut"]
vegetables =    ["celery", "carrots", "potatoes"]
meats =     ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

for i in groceries:
    for x in i:
        print(x, end=" ")
    print()
       

#print(fruits[1])
#print(meats[0])
#print(groceries[0][3])
#print(vegetables[:2])

""

#lets crate a calculater pad number. we would use turple cos they are ordered and unchangeable

pad_num = ((1, 2, 3), (4, 5, 6), (7, 8, 9), ("*", 0, "#"))

for i in pad_num:
    for row in i:
        print(row, end=" ")
    print()
    print()
    print()
""


#print(help(__name__))


##Dictionary

capitals = {"USA" : "washinton",
            "India" : "New Delhi",
            "Nigeria" : "Abuja"}

print(capitals.get("USA"))
capitals.update({"Germany" : "Berlin"})
capitals.update({"Nigeria" : "Lagos"})

for key in capitals.keys():
    print(key)

capitals.pop("Nigeria")

for key, value in capitals.items():
    print(f"{key}, {value}")



items = capitals.items()
print(items)
print(capitals)
""

#lets generate a random guessing game. to generate a random number, we can import the random module

import random

#print(help(random)) | setstate #we can print the help method to see all the available methods available within the Random module

options = ["Rock", "Paper", "Scissors", "book", "garri"]
cards = ["a", "3", "b", "c", "1", "4", "6", "w"]

random.shuffle(cards) #using the .choice() or .shuffle() methods to

#number = random.randint(1,50) # random between 1 and 50 using the .randint() method
#number = random.random() #random between floating number of 0 and 1 using the .random() method


#print(number)
print(cards)

#for i in options:
 #   print(options)

""
def happy(name):
    print(f'happy bithday {name}')
    print("Happy birthday friend")

happy("ola")
""
import time 

def count(start, end):
    for x in range(start, end):
        print(x)
        time.sleep(1)
    print("DONE")

count(10, 20)
""

def name(*args):
    for arg in args:
        print(arg, end=" ")

name("ola", "olu", "yusuf")
print()
""

#define a shipping label using both *args and **kwargs
def shipping_labels(*args, **kwargs):
    for arg in args:
        print(arg, end="")
    print()
    for value in kwargs.values():
        print(value, end=" ")
    print()

    print(f"{kwargs.get('street')} {kwargs.get('city')}, {kwargs.get('country')}")

shipping_labels("Mr.", "OLa", "daya",
                street="68 Brompton str.",
                city="london",
                country="united Kingdon")
""

grades = {"sandy": "A",
          "patrick": "B",
          "ola": "C",
          "odun": "D"}

while True: 

    student = input("Enter student name here: ")

    if student in grades:
        print(f"{student}'s grade is {grades.get(student)}")
    else:
        print(f"{student} grade NOT AVAILABLE")
""

email = input("Enter your email address: ")

if "@" in email and "." in email:
    print(f'{email} is valid')
else:
    print("invalid email")

""
running = True

while running:

    def day_of_week(day):
        match day:
            case 1:
                return f'Its a Monday'
            case 2:
                return f'Its a Tuesday'
            case 3:
                return f'Its a wesday'
            case 4:
                return f'Its a Thursday'
            case 5:
                return f'Its a friday'
            case 6:
                return f'Its a saturday'
            case 7:
                return f'Its a Sunday'
            case _:
                running = False
                print(f"INVALID DATE")
                
        

    day = int(input("Enter the day of the week in Number 1 - 7: "))   
    print(day_of_week(day))
""

def is_weekend(days):
    match days:
        case "monday" | "Tuesday" | "Wenesday" | "Thursday" | "Friday":
            return True
        case "Saturday" | "Sunday":
            return False
        case _: 
            return False
        

print(is_weekend("mpizza"))
""

#to see all the built in modules, run

#print(help("math"))

import our_example

x = our_example.square(3)

print(x)

""

def favourite_food(food):
    print(f" Your favourtae food is {food}")

def main():
    print("Hello")
    favourite_food("EBA")
    print("Goodbye")



if __name__ == "__main__":
    main()

""

#Testing working with dictionary again

capitals = {"USA" : "washinton",
            "India" : "New Delhi",
            "Nigeria" : "Abuja"}

for i in capitals:
    print(capitals[i])

print()
for i in capitals:
    print(i)

for i, x in capitals.items():
    print(f' {i} : {x}')

""

x = range(10)

for i in x:
    if i % 2 == 0:
        continue
    print(i)
""

import random

symbols = ["⭐", "💎", "🍋", "🍒", "🍊", "🍉",]

results = [random.choice(symbols) for i in range(3)]

print(results)
""


#print(help(list))

hint = ["3",'2','1','4','5','6','7','8','9',]
print("|".join(hint))


print(dir(list))
print()
print(dir(str))
print(dir(set))
""

#importing car class from the car.py

from car import car

car1 = car("toyota", '2022', "green", False) #creating  object called car1
car2 = car("Corvette", 2025, "blue", True)
car3 = car("Charger", 2020, "yello", True)



print(car1)
print(car1.model)
print(car1.for_sale)
print(car2.year)
print(car2.for_sale)
""

print(dir("python"))

print()
print()
print(dir(60))
"""

#####Multithreading

import threading
import time

def walk(first, last):
    time.sleep(8)
    print(f"YOU WALK THE DOG {first}, {last}")

def trash():
    time.sleep(2)
    print("you take out the trash")

def mail():
    time.sleep(4)
    print("you get the mails")

chore1 = threading.Thread(target=walk, args=("ola", "olufowobi",)) #using the thread method within the threading module to pass put walk function as target
chore1.start() #calling the thread to start

chore2 = threading.Thread(target=trash) #using the thread method within the threading module to pass put walk function as target
chore2.start() #calling the thread to start

chore3 = threading.Thread(target=mail) #using the thread method within the threading module to pass put walk function as target
chore3.start() #calling the thread to start

chore1.join() #the join() method ensure the choice1, choice2, and choice3 completes before continuing with the rest of the programe. i.e, the print statement
chore2.join()
chore3.join()

print("All cloice complaet")