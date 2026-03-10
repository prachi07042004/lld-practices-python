''' 
  LSP(Liskov Substitution Principle) - states that objects of the parent class should be replacable with the objects of the child class without breaking the program.
  -If child class is-a parent class, then child should work exactly like parent
  -You should be able to use child class wherever parent class is expected.
  -Child class should not break the behavior the parent class promises.
  No class should be forced to implement methods it doesn't use.
  Split large interfaces into smaller, more specific ones.

  Ex: Bird an abstract class with abstract methods eat() and fly(), a child class Penguin() cannot fly!(raise an exception) contradicts LSP
  Ex: Bank Account(interface) with abs methods deposit and withdraw-> child class FD raises and exception for withdraw method!
'''
from abc import ABC, abstractmethod

class BankAccount(ABC):
  def __init__(self, balance:int):
    self.balance:int = balance

  @abstractmethod
  def withdraw(self, amount):
    pass

  @abstractmethod
  def deposit(self, amount):
    pass

class SavingsAccount(BankAccount):
  def __init__(self, balance: int):
    super().__init__(balance)

  def withdraw(self, amount):
    if self.balance < amount:
      print("Cannot withdraw, insufficient balance")
    else:
      self.balance -= amount
      print(f"Amount withdrawn, remaining balance {self.balance}")

  def deposit(self, amount):
    self.balance += amount
    print(f"Amount deposited, remaining balance {self.balance}")

class FixedDepositAccount(BankAccount):
  def __init__(self, balance: int):
    super().__init__(balance)

  def withdraw(self, amount):
    raise Exception("Cannot withdraw from FD")

  def deposit(self, amount):
    self.balance += amount
    print(f"Amount deposited, remaining balance {self.balance}")

# s = SavingsAccount(1000)
# s.deposit(300)
# s.withdraw(200)

fd = FixedDepositAccount(1000)
fd.deposit(600)
fd.withdraw(100)
