'''
  ISP(interface segregation principle) - Koi class mein bas wahi methods do jo usko necessary hai not more than that
  -ensures that classes are not forced to implement those methods which it doesn't need.
  -break large general purpose interface into small specific ones.
  -benifits- maintainability, flexibility, testability.
  -classes should only depend on methods they actually use.

  The Liskov Substitution Principle (LSP) and Interface Segregation Principle (ISP) differ primarily in focus: LSP ensures that derived classes can fully substitute their base classes without breaking functionality (focus on inheritance/subtyping), while ISP ensures clients do not depend on methods they do not use (focus on interface design/separation).
'''

from abc import ABC, abstractmethod

class Employee(ABC):
  
  @abstractmethod
  def eat(self):
    pass

  @abstractmethod
  def work(self):
    pass


class Worker(Employee):
  def eat(self):
    print("Worker is eating")

  def work(self):
    print("Worker is working")


class Robot(Employee):
  def eat(self):
    raise Exception("Robot can't eat!")

  def work(self):
    print("Robot is working")

r = Robot()
r.eat()
