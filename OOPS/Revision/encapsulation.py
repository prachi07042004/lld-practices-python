'''
  Encapsulation - protecting the internal data of class, you control what the outside world can see and what it cannot. This prevents accidental modification of important data
  -Data and method that operates on that data are bundled inside a class
  -Sensitive data marked private so it can't be accessed directly from outside
  -Access is given through controlled methods called getters and setters.
  -Makes code more secure and presictable.
  -ex: ATM machine you can check balance and withdraw but you can't access the bank's internal system directly
  Put double underscore to make an attribute private(can be accessed from inside only)
  Getters and setters are methods used to protect data and control access to class fields (encapsulation) by providing public methods to read (getter) or update (setter) private variables.

  Different access modifiers

  -Public - No leading underscore (e.g., name), Accessible from anywhere, inside or outside the class. All members are public by default.

  -Protected - Single leading underscore (e.g., _name), Accessible within the class and by its subclasses.designed specifically to be accessible by subclasses, as well as any other classes within the same package (in languages like Java).

  -Private -Double leading underscores (e.g., __name), Accessible only within the class where defined. Python uses name mangling to achieve this, changing the attribute name internally (e.g., __name becomes _ClassName__name) to avoid conflicts in subclasses.
'''

class Bank:
  def __init__(self, name:str, balance: int):
    self.name:str = name
    self.__balance:int = balance

  #private method
  def __isServerLive(self):
    return True

  def deposit(self, amount:int):
    if self.__isServerLive == True:
      self.__balance += amount
      print(f"Amount deposited, current balance = {self.__balance}\n")
    else:
      print("Server is down")


  def withdraw(self, amount: int):
    if self.__balance < amount:
      print("Insufficient balance\n")
    else:
      self.__balance-=amount
      print(f"Amount withdrawn, current balance = {self.__balance}\n")

  #Getter
  def get_balance(self):
    print(f"Current balance = {self.__balance}")

  #Setter 
  def set_balance(self, new_amount):
    self.__balance = new_amount


acc = Bank("Prachi", 1000)
acc.deposit(1000)
acc.withdraw(1500)
acc.get_balance()
acc.set_balance(20000)
#acc.__isServerLive() #Gives error
