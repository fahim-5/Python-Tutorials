"""
Object-Oriented Programming (OOP) Methods in Python

This file demonstrates the three types of methods in Python's OOP:
1. Instance methods
2. Class methods
3. Static methods
"""

class Dog:
    # Class attribute
    total_dogs = 0
    scientific_name = "Canis lupus familiaris"
    
    def __init__(self, name, breed):
        """Instance initializer (special instance method)"""
        self.name = name      # Instance attribute
        self.breed = breed    # Instance attribute
        Dog.total_dogs += 1   # Modifying class attribute
        
    # 1. Instance Method
    def bark(self):
        """Instance method - operates on instance data"""
        print(f"{self.name} says woof!")
    
    def get_description(self):
        """Another instance method using instance attributes"""
        return f"{self.name} is a {self.breed}"
    
    # 2. Class Method
    @classmethod
    def create_anonymous_dog(cls):
        """Class method that acts as an alternative constructor"""
        return cls("Anonymous", "Unknown breed")
    
    @classmethod
    def get_scientific_name(cls):
        """Class method accessing class attribute"""
        return cls.scientific_name
    
    @classmethod
    def get_total_dogs(cls):
        """Class method that works with class state"""
        return cls.total_dogs
    
    # 3. Static Method
    @staticmethod
    def is_dog_sound(sound):
        """Static method - utility function about dogs"""
        return sound.lower() in ["woof", "bark", "ruff"]
    
    @staticmethod
    def dog_years_to_human(years):
        """Static method - performs calculation"""
        return years * 7


# ===== Demonstration =====

if __name__ == "__main__":
    print("\n=== Instance Methods ===")
    dog1 = Dog("Rex", "German Shepherd")
    dog1.bark()  # Calling instance method
    print(dog1.get_description())
    
    print("\n=== Class Methods ===")
    # Using class method as alternative constructor
    anonymous = Dog.create_anonymous_dog()
    print(f"Anonymous dog created: {anonymous.get_description()}")
    
    # Accessing class method
    print(f"Scientific name: {Dog.get_scientific_name()}")
    print(f"Total dogs created: {Dog.get_total_dogs()}")
    
    print("\n=== Static Methods ===")
    # Using static methods
    sound = "Woof"
    print(f"Is '{sound}' a dog sound? {Dog.is_dog_sound(sound)}")
    print(f"5 dog years = {Dog.dog_years_to_human(5)} human years")
    
    # Static methods can also be called on instances
    print(f"7 dog years = {dog1.dog_years_to_human(7)} human years")
    
    print("\n=== Summary ===")
    print("""
Key Differences:
1. Instance Methods:
   - Require 'self' parameter
   - Can access and modify instance and class attributes
   - Most common method type
    
2. Class Methods:
   - Decorated with @classmethod
   - Require 'cls' parameter
   - Can only access and modify class attributes
   - Often used as alternative constructors
    
3. Static Methods:
   - Decorated with @staticmethod
   - No 'self' or 'cls' parameter
   - Can't modify instance or class state
   - Act as utility functions in class namespace
""")