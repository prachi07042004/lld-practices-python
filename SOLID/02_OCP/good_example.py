'''
  Architecture - Parent Class PaymentMethods -> child classes UPI, Credit_Card, Net_Banking
  Now we need to define method pay in all the child classes so we can create an abstract method pay in the parent class.
  A class PaymentProcesser - it will take PaymentMethods as object and call pay method through it
  Now if we want to add a new method ex. PayPall we can easily create a child class of PaymentMethods 
  This way it will not be required to modify any of the other classes!
'''

from abc import ABC, abstractmethod

class PaymentMethod(ABC):

  @abstractmethod
  def pay(self, amount:int):
    pass

class UPIPayment(PaymentMethod):
  def pay(self, amount:int):
    print(f"Paying through UPI of Rs.{amount}")

class DebitCardPayment(PaymentMethod):
  def pay(self, amount:int):
    print(f"Paying through DebitCard of Rs.{amount}")

class CreditCardPayment(PaymentMethod):
  def pay(self, amount:int):
    print(f"Paying through CreditCard of Rs.{amount}")


class PaymentProcessor:
  def process_payment(self, payment_method: PaymentMethod, amount:int):
    payment_method.pay(amount)

debit = DebitCardPayment()
credit = CreditCardPayment()

paym_processor = PaymentProcessor()
paym_processor.process_payment(debit, 25000)

