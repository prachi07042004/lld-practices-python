'''
  Inheritance - allows one(child) class to acquire properties and methods of another(parent/base) class
  changes made in parent class automatically reflect in child classes

  The super keyword in inheritance is a reference variable used to access the immediate parent class's members (methods, fields, and constructors) from a subclass, promoting code reusability and resolving naming conflicts. It is commonly used to invoke parent constructors (super()) or override methods (super.method()).

  Polymorphism - Poly(many), Morphs(forms) - allows same method name to behave differently based on which object calls it 
  Same method name works differntly for differnt classes 
  You don't need to remember different multiple method names for similar actions
  Method Overriding - child class provides it's own version of a parent's method
  Ex: a draw() method on a circle draws a circle, on a rectangle it draws a rectangle-same name different behavior
'''

class Animal:

  def __init__(self, name: str, age: int ):
    self.name = name
    self.age = age

  def eat(self):
    print("I am eating ")

  def sleep(self):
    print("I am sleeping")

  def move(self):
    print("I am moving")

class Dog(Animal):

  def __init__(self, name: str, age: int, breed: str):
    super().__init__(name, age)
    self.breed = breed

  def bark(self):
    print("I am barking")

  def display(self):
    print(f"Name is {self.name}, Age is {self.age}")

  def move(self):
    print("I move on 4 legs")

dog = Dog("Whiskey", 4, "labrador")
dog.eat()
dog.bark()
dog.display()
dog.move() #calls move of dog
