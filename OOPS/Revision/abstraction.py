'''
Abstraction is about reducing complexity. You expose only the necessary details to the user and hide all the complicated internal logic. The user doesn't need to know how things work inside , just that they work

An abstract class can have any number of abstract and non-abstract methods, or even no abstract methods at all.
Any non-abstract (concrete) class that inherits from an abstract class must provide implementations for all of the inherited abstract methods, or it must also be declared as an abstract class.
The primary characteristic of an abstract class is that it cannot be instantiated on its own; it must be subclassed. 

It is a module (abc) and a class (ABC) used to define blueprints for other classes, enforcing that subclasses implement specific methods. By inheriting from abc.ABC and using the @abstractmethod decorator, you prevent direct instantiation of the base class and ensure consistent interfaces.

Module: import abc allows for the creation of abstract classes.
Class: abc.ABC is a helper class that allows you to create an abstract base class by inheriting from it.
Metaclass: abc.ABCMeta is the underlying metaclass that handles the creation and behavior of these classes.
Decorator: @abc.abstractmethod marks methods that must be overridden in subclasses.
what are decorators? they wrap the function or class to add extra functionality without changing its core code.
'''

from abc import ABC, abstractmethod

class Shape(ABC):

  @abstractmethod
  def area(self):
    pass

  @abstractmethod
  def perimeter(self):
    pass

# s = Shape() #Gives error - cannot instantiate abstract class

class Rectangle(Shape):
  def __init__(self, length:int, breadth: int):
    self.length = length
    self.breadth = breadth

  def area(self):
    print(self.length * self.breadth)

  def perimeter(self):
    print(2* (self.length + self.breadth))

r = Rectangle(3,4)
r.area()
r.perimeter()

class Circle(Shape):
  def __init__(self, radius:int):
    self.radius = radius

  def area(self):
    print(3.14 * (self.radius)**2)

  def perimeter(self):
    print(2* 3.14* self.radius)
  
c = Circle(4)
c.area()
c.perimeter()

