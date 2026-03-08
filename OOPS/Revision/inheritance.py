'''
  Inheritance - allows one(child) class to acquire properties and methods of another(parent/base) class
  changes made in parent class automatically reflect in child classes

  The super keyword in inheritance is a reference variable used to access the immediate parent class's members (methods, fields, and constructors) from a subclass, promoting code reusability and resolving naming conflicts. It is commonly used to invoke parent constructors (super()) or override methods (super.method()).
'''

class Animal:

  def __init__(self, name: str, age: int ):
    self.name = name
    self.age = age

  def eat(self):
    print("I am eating ")

  def sleep(self):
    print("I am sleeping")

class Dog(Animal):

  def __init__(self, name: str, age: int, breed: str):
    super().__init__(name, age)
    self.breed = breed

  def bark(self):
    print("I am barking")

  def display(self):
    print(f"Name is {self.name}, Age is {self.age}")


dog = Dog("Whiskey", 4, "labrador")
dog.eat()
dog.bark()
dog.display()

  