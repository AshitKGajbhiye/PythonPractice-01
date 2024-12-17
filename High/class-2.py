'''
__str__() method
Python has a particular method called __str__(). that is used to define how a class object should be represented as a string. It is often used to give an object a human-readable textual representation, which is helpful for logging, debugging, or showing users object information. When a class object is used to create a string using the built-in functions print() and str(), the __str__() function is automatically used. You can alter how objects of a class are represented in strings by defining the __str__() method.
Class attributes: Class attributes belong to the class itself they will be shared by all the instances. Such attributes are defined in the class body parts usually at the top, for legibility.
'''
class GFG:
    def __init__(self, name, company):
        self.name = name
        self.company = company

    def __str__(self):
        return f"My name is {self.name} and I work in {self.company}."

my_obj = GFG("John", "GeeksForGeeks")
print(my_obj)
