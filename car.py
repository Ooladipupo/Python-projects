#this will be imported into the main pyton file to use this class overthere

class car:
    def __init__(self, model, year, color, for_sale): #This is a constructor method used to define our class attributes
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def __str__ (self):  # __str__ is a built in method that return a default value when no other function is defined to be called within the class
        return self.year


    def my (self):
        return f'i drive a {self.model} model of {self.year}'