from abc import ABC, abstractmethod

class Workable(ABC):
  @abstractmethod
  def work(self):
    pass

class Eatable(ABC):
  @abstractmethod
  def eat(self):
    pass

class Worker(Workable, Eatable):
  def eat(self):
    print("Worker is eating")

  def work(self):
    print("Worker is working")

class Robot(Workable):
    def work(self):
      print("Robot is working")

w = Worker()
w.eat()
w.work()

r = Robot()
r.work()