''' 
  Architecture
  -Account interface - abs method (deposit)
  -WithdrwableAccount interface - abs method (withdraw)
  -class SavingsAccount(WithdrawableAccount) - needs to implement both withdraw() and deposit()
  -class FixedDepositAccount(Account) - needs to implement only deposit()
'''

from abc import ABC, abstractmethod

class Account(ABC):
  def __init__(self, balance:int):
    self.balance = balance

  @abstractmethod
  def deposit(self, amount):
    pass

