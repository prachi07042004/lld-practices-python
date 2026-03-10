''' 
OCP (Open Close Principle) - software entities (classes, modules, functions) should be open for extension but closed for modification.
Open for Extension = You can add new features easily
Closed for modification = Don't change existing working code (that must have been already tested, modifying it can lead to bugs)
Ex:Adding new payment methods (Credit card, UPI, PayPal) without modifying the existing payment processing code!

If in future we need to add a new payment method then we will have to modify the existing code which is a bad practice.
'''

class PaymentProcessor:
  def pay(self, payment_method:str, amount: int):
    if payment_method == "UPI":
      print(f"Starting UPI transcation of Rs.{amount}")
      print("UPI transaction finished!")
    if payment_method == "credit_card":
      print(f"Starting credit_card transcation of Rs.{amount}")
      print("credit_card transaction finished!")
    if payment_method == "net_banking":
      print(f"Starting net_banking transcation of Rs.{amount}")
      print("net_banking transaction finished!")

pay_p = PaymentProcessor()
pay_p.pay("UPI", 1000)
