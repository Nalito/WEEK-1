# Data Structures in python

## Lists []
ages = [12, 34, 45, 66, 32, 25, 45, 76]
########0   1   2   3   4   5   6   7   

print(ages)

# Access the first element
print(ages[0])

# Access the last element
print(ages[-1])

# Subset a list
print(ages[0:5])

# Pop from a list
# Pop is limited to the last index
ages = [12, 34, 45, 66, 32, 25, 45, 76]
print(ages.pop())
print(ages)

# Delete from a list using a specific index
ages = [12, 34, 45, 66, 32, 25, 45, 76]
print(ages)
del ages[-3]
print(ages)

# Append to a list
# Fixes a value to the end. Limited to one value at a time
ages = [12, 34, 45, 66, 32, 25, 45, 76]
ages.append(100)
print(ages)

# Extend a list
# It is not limited to one value at a time
ages = [12, 34, 45, 66, 32, 25, 45, 76]
ages.extend([65, 88, 44, 78, 90, 32])
print(ages)

# Insert into a list
ages = [12, 34, 45, 66, 32, 25, 45, 76]
ages.insert(3, 55)
print(ages)


## Dictionaries
my_dict = {'name': 'James Bond', 'age': 55, 'contact': ['jb@hotmail.com', 55545898]}
print(my_dict)

# Access the first element
# print(my_dict[0])
print(my_dict['age'])

# Access the last element
print(my_dict['contact'])

# Accessing elements using .get()
my_dict = {'name': 'James Bond', 'age': 55, 'contact': ['jb@hotmail.com', 55545898]}
print(my_dict.get('age'))

# Key-value objects
# Fetch the keys from a dictionary
print(my_dict.keys())

# Fetch the values from a dictionary
print(my_dict.values())

# Fetch the key-value pairs from a dictionary
print(my_dict.items())

my_dict = {'name': 'James Bond', 'age': 55, 'contact': ['jb@hotmail.com', 55545898]}
keys = []
values = []
for key, value in my_dict.items():
    keys.append(key)
    values.append(value)

print(keys)
print(values)

# Add to a dictionary
# dictionary_name['new_key'] = 'new_value'
my_dict = {'name': 'James Bond', 'age': 55, 'contact': ['jb@hotmail.com', 55545898]}
my_dict['is_student'] = False
print(my_dict)

# Delete from a dictionary
del my_dict['is_student']
print(my_dict)


## Tuples
tup = ('introduction', 'to', 'artificial', 'intelligence')
print(tup)

# Tuples are ordered
print(tup[0])
print(tup[-1])

# Tuples are unchangeable
scores = (45, 70, 66)
print(scores)
# Convert to list
scores = list(scores)
# I want to change the first index to 50
scores[0] = 50
# Convert back to tuple
scores = tuple(scores)
print(scores)

## Sets are unordered and changeable/mutable
fruits = {'apple', 'mango', 'guava', 'banana', 'orange'}
print(fruits)

# Add to a set
fruits.add('watermelon')
print(fruits)


# Sets cannot have duplicate values
scores = {2, 3, 4, 2, 4, 3, 5, 3, 5}
print(scores)

#Union
set1 = {1, 3, 5, 7}
set2 = {2, 4, 6, 8, 5}
print(f"Set 1: {set1}")
print(f"Set 2: {set2}")

print(set1.union(set2))

# Intersection
print(set1.intersection(set2))

# Difference
print(set1.difference(set2))
print(set2.difference(set1))

# Clear
set1.clear()
print(set1)

# Strings
sample = 'Today is Sunday. Sunday is good for learning AI!'
print(sample)

# lower
print(sample.lower())

# upper
print(sample.upper())

# title
print(sample.title())

# strip - it removes leading and trailing whitespaces
sample = "This is an AI day."
print(sample)
print(sample.strip())

# split - it divides a string based on a query
print(sample.split("AI"))

# join - to adds a character/space to a string
print(" ".join(sample))

# replace - used to replace a string with another string
print(sample.replace("AI", "ML"))



# Object Oriented Programming
## Creating a class
class Car:
    # Class attribute
    cat = "Vehicle"

    # Constructor method
    def __init__(self, brand, model):
        # Instance attributes
        self.brand = brand
        self.model = model

    # Method
    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}")

# Creating objects of the Car class
car1 = Car("Toyota", "Corolla")
car2 = Car("Honda", "Civic")
car3 = Car("Vogue", "Range Rover")

# Accessing class attribute
print(Car.cat)

# Accessing instance attributes
car1.display_info()
car2.display_info()
car3.display_info()


## Main Principles of OOP
# Encapsulation
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def get_make(self):
        return self.make

    def get_model(self):
        return self.model

car = Car("Toyota", "Corolla")
print(car.get_make()) 
print(car.get_model())


class Food:
    def __init__(self, name, origin, rating):
        self.name = name
        self.origin = origin
        self.rating = rating

    # Returns the rating of a food
    def fetch_rating(self):
        return self.rating  
    
    # Change the rating of a food
    def change_rating(self, rating):
        self.rating = rating
        return self.rating
    
    # Change origin of a food
    def change_origin(self, origin):
        self.origin = origin
        return self.origin
    
# Create 3 objects of the Food class
amala = Food('amala', 'Nigeria', 9)
baugette = Food('baugette', 'Italy', 8)
noodles = Food('noodles', 'China', 7)

# Change origin of baugette
print(baugette.change_origin('France'))

# Change the rating of amala
print(amala.change_rating(10))

# Fetch the rating for noodles
print(noodles.fetch_rating())


# Polymorphism
# Super class - the class that all other classes inherit from
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow..."

def animal_sound(animal):
    return animal.make_sound()

dog = Dog()
print(animal_sound(dog))

cat = Cat()
print(animal_sound(cat))


# Modularity
import math_operations

print(math_operations.add(5, 3))     
print(math_operations.subtract(5, 3)) 
print(math_operations.multiply(5, 3))  
print(math_operations.divide(6, 3)) 
print(math_operations.power_of(2, 4))


# Inheritance
# Superclass
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def bark(self):
        return "Woof"
    
class Lhasa(Dog):
    def fur(self):
        return "Long fur"
    
class Bird(Animal):
    def chirp(self):
        return "Chirp"
    
lhasa = Lhasa()
print(lhasa.speak())
print(lhasa.bark())
print(lhasa.fur())
    
bird = Bird()
print(bird.speak())
print(bird.chirp())

dog = Dog()
print(dog.speak()) 
print(dog.bark())  

## Abstraction
import mymodule

# Using function from the module
mymodule.greet("Alice")

# Creating object of MyClass from the module
obj = mymodule.MyClass(5)
print(obj.x)