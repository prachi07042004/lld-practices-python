from withdrawable_account import WithdrawableAccount

class Savings_Account(WithdrawableAccount):

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