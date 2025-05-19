#creating a class called Myclass that has the initiator function that has 2 properties name and age
class Myclass:
    def __init__(self, name, age):              #self allows us to establish a variable in one method and use it in other methods
        self.name = name
        self.age = age

    def get_name_age(self):
        print(f" my school name is {self.name} and aged {self.age}")   #the self made it possible to call the 2 varieables initially declared in the above init method

#creting an object using the defined class. we would called the object Nursery. 
# giving that the class initaitor accepts 2 proprties name and age, we need to include it when creating our nursery object
# as you would see in parenthesis below 

nursery = Myclass("ade", 23)
reception = Myclass("happylittlesumbeam", 44)

print (nursery.name)

nursery.get_name_age()
reception.get_name_age()