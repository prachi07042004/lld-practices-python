from account import Account

class FixedDepositAccount(Account):
  def __init__(self, balance: int):
    super().__init__(balance)

  def deposit(self, amount):
    self.balance += amount
    print(f"Amount deposited, remaining balance {self.balance}")