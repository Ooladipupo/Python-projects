"""

class car:  #going forward, always mak sure a class is capitalize for the first letter. eg class Car

    best_car = "bens" #class variable
    num_of_cars = 0

    def __init__(self, model, year, color, for_sale): #This is a constructor method used to define our class attributes
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale
        car.num_of_cars += 1    #we want to increatement the numofcar varaible with the objects created out of this car class

    def __str__ (self):  # __str__ is a built in method that return a default value when no other function is defined to be called within the class
        return self.year


    def my(self):
        return f'You drive the car'

car1 = car("toyota", '2022', "green", False) #creating  object called car1
car2 = car("Corvette", 2025, "blue", True)
car3 = car("Charger", 2020, "yello", True)


print(f'My car business has {car.num_of_cars} in stock, name')
print()

print(car1.model)
print(car2.model)
print(car3.model)
print()
print(car1.for_sale)
print(car2.year)
print(car2.for_sale)
print(car.best_car) #we are priniting the class variable best_car directly from the car class. 
print(car.num_of_cars)
""


###Class Inherritace
###lets create an ANIMAL CLASS to eb inherirted by different types of animale we know of

class Animal: 
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f'{self.name} is eating')

    def sleep(self):
        print(f'{self.name} is sleeping')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Mouse(Animal):
    pass


dog = Dog("Skubido")
cat = Cat("Garfield")
mouse = Mouse("Mickey")


print(dog.name)
print(dog.is_alive)
dog.eat()
dog.sleep()

""

#MUlti inheritance and Multiple level inheritance. prey and predators are parents. while rabbit and hawks are childreen classes. 
# lets also create another class called Animal (like a grand parent) and make the prey and preditor class to inherrit from the animal calss
# we eould also incluse a constructor within the animal class to assign an paramrter to accept the name attributes

class Animal:

    def __init__(self, name):
        self.name = name 


    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")


class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")


class Predator(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")

class Rabbit(Prey):
    pass

class Hawk(Predator):
    pass


class Fish(Prey, Predator):   #multi inheritance from both prey and predators class
    pass


#Lets create objects now

rabbit = Rabbit("Buby")
hawk = Hawk("Bingo")
fish = Fish("Brim")

rabbit.eat()
hawk.hunt()
fish.sleep()

rabbit.eat()

""


#lets learn the super() function used in a child class to call methods from a parent class. 

class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def descibe(self): 
        print(f"it tttttttis {self.color}")

class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    def descibe(self): 
        super().descibe()
        print(f"it is a circle with an area of {3.142 * self.radius ** 2}")
        

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def descibe(self): 
        super().descibe()
        print(f"it is a square with an area {self.width * self.width}")

class Trainagle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def descibe(self): 
        super().descibe()
        print(f"it is a Traingle with an area {self.width * self.height}")


circle = Circle("green", "Yes", 3.142)
square = Square("yello", "Yes", 3.142,)
traingle = Trainagle("orange", "Yes", 2, 8)


circle.descibe()
print(square.descibe())
print(traingle.descibe())


""
## Lets study polimorphism. meaning to have multiple form 


from abc import ABC, abstractmethod   #The abc module in Python stands for Abstract Base Classes. It provides a way to define abstract classes, which are classes that cannot be instantiated directly but serve as blueprints for other classes.



class Shape:

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.142 * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height
    

class Pizza(Circle): #creating a shape thats completely unrelated to the shape objects. to use the area method of the Circle Class, we make the Pizza class to Inherit from the Circle class
    def __init__(self, topping, radius):        #Pizza could fit in as a shape also, reason we used the circle class as inherritance
        super().__init__(radius)
        self.topping = topping
        


circle = Circle(25)  #our circle object inheritad from the Circle class as well as from the shape class. meaning our object here can take 2 forms
square = Square(20)  #our square can take 2 forms namely the Square class and the Shape class but cant be a Circle or Trangle class
triangle = Triangle(20, 30)
pizza = Pizza("peperroni", 3.2)

#shapes = [Circle(), Square(), Triangle()] #creating a list of shape objets
shape = [circle.area(), square.area(), triangle.area(), pizza.area()]

print(shape)

for i in shape:
    print(f'{i}cm2')

""

##Peacticing duck typing. if it looks like a duck and quack like a duck, it must be a duck

class Animal:
    alive = True

class Dog(Animal):
    def speak(self):
        print("Woof")


class Cat(Animal):
    def speak(self):
        print("MEOW")

class Car:

    alive = False
    def speak(self):
        print("HONK")

animals = [Dog(), Cat(), Car()]

for animal in animals:
    animal.speak()
    print(animal.alive)

""


###Staticl Methods ()


class Employee:

    def __init__(self, name, position):
        self.name = name
        self.position = position

    def get_info(self):  #we defined an instance method
        return f"{self.name} = {self.position}"
    

    @staticmethod  #defining a static method
    def is_valid_position(position):  #being  static methos, we dont need to include the self attributes, as this method/function does not need an acces to the main class data
        valid_position = ["Manager", "Cashier", "Cook", "Janitor"]
        if position in valid_position:
            return "great"
    
print(Employee.is_valid_position("Cook"))  #calling the staticmathod is different from the way we call intance method 
                                            #as we dont need to create an object from that class for a static method to call the method. all we need is the class
                                            #name (Employee) and the static method name. No need for an object

employee1 = Employee("Eugine", "Manager")  #creating objects
employee2 = Employee("Mark", "Auditor")

#to print out the instance method, we need to first call the Object (employee1, employee2, as above), followed by the instance method 

print(employee1.get_info())  #we are calling the instance method get_info()
print(employee2.get_info())

""

##Learing Class Method

class Student:
    
    count = 0
    total_gpa = 0

    #defining the constructor
    def __init__(self, name, gpa):
        self.name =name
        self.gpa = gpa
        Student.count += 1 #to increment the count variable by 1 for any object created from this class
        Student.total_gpa += gpa

    #INTANCE METHOD
    def get_info(self):
        return f'{self.name} {self.gpa}'
    
    @classmethod
    def get_count(cls):
        return f'Total number of student: {cls.count}'
    

    @classmethod
    def get_average_gpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f'{cls.total_gpa / cls.count:.2f}'

    

    
student1 = Student("Bayo", 3.2)
student2 = Student("Bashirat", 4.2)
student3 = Student("Aina", 3.5)
student4 = Student("Wasiuu", 5.2)

print(Student.get_count())

print(Student.get_average_gpa())



""

##learning @property to read, write, and delete attributes using the getter, setter, and deleter method

class Rectangle:
    

    def __init__(self, width, height):  #this Rectangle class accept two parameters width ans height
        self._width = width
        self._height = height


    @property
    def width(self):
        return f'{self._width:.1f}cm'
    
    @property
    def height(self):
        return f'{self._height:.1f}cm'

ractangle = Rectangle(3, 4)

print(ractangle.height)
print(ractangle.width)

"""


###Decorator


#lets create a sprincle decorator to be addeded to the base function get_ice_cream

#creating the decorator first
def add_sprincles(func):
    def wrapper(*args, **kwargs):       #args and kwargs to accespt any form of arguement
        print("You add sprincles")
        func(*args, **kwargs)
    return wrapper

#creating another decorator
def add_fudge(func):
    def wrapper(*args, **kwargs):         #nested function
        print("you had fufu")
        func(*args, **kwargs)
    return wrapper


@add_fudge   #adding the add_fudge and add_sprincle functions to the base function
@add_sprincles
def get_ice_cream():                    #starting with the base function
    print("Here is your ice cream")


get_ice_cream()