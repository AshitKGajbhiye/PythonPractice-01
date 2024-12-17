'''
Aspect : Definition

    Class Method: A method bound to the class itself, defined with "@classmethod"
    Static Method: A method that does not receive an implicit first argument ('self' or 'cls'), defined with "@staticmethod"
    Instance Method: A method defined within a class, taking `self` as the first parameter, representing the instance.

Access

    Class Method: Can access class attributes and modify them.
    Static Method: Cannot access or modify class or instance attributes.
    Instance Method: Can access and modify instance attributes.

First Argument

    Class Method: Receives 'cls' as the first argument representing the class.
    Static Method:No implicit first argument is passed to the method.
    Instance Method: Receives `self` as the first argument representing the instance.

Usage

    Class Method: Often used for operations that modify or interact with class-level data.
    Static Method: Typically used for utility functions that don't depend on instance or class state.
    Instance Method: Commonly used for operations specific to individual instances.

Inheritance

    Class Method: Can be overridden in subclasses, with 'cls' referring to the subclass.
    Static Method: Can be called directly via the class or subclass, but not overridden.
    Instance Method: Can be overridden in subclasses, with 'self' referring to the subclass instance.

Access Modifier

    Class Method: Typically used when the method needs access to class-level data.
    Static Method: Suitable when the method doesn't rely on instance or class attributes.
    Instance Method: Preferred when the method operates on instance-specific attributes.

Example Use

    Class Method: Calculating statistics across all instances of a class.
    Static Method: Formatting dates, performing mathematical operations.
    Instance Method: Returning information specific to an instance, like its attributes.

Usefulness

    Class Method: Useful when dealing with class-level functionality and shared attributes.
    Static Method: Handy for standalone functions related to the class but not dependent on its state.
    Instance Method: Essential for modifying and accessing instance attributes and behaviors.
'''

class Animals:
    # class Attribute
    home = 'Zoo'

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Creating a class method
    @classmethod
    def animals_home(cls, home):
        cls.home = home

    # Instance method
    def insta_method(self):
        # Modifying the class attribut
        self.home = 'Jungle'
        return f'Name: {self.name}, Age: {self.age}, Location: {self.home} '
    
    @staticmethod
    def check_age(age):
        if age > 5:
            return 'Adult'
        else:
            return 'Not Adult'
        
#creating Animal instances
animal1 = Animals("Lion", 4)
print(animal1.insta_method())

# calling static method using class instance
print(animal1.check_age(4))

'''Output:
Name: Lion, Age: 4, Location: Jungle 
Not Adult
'''