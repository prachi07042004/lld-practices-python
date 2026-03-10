'''
  SRP (single responsibility principle) - a class should have only one reason to change. Don't make a class do everything, Each class should focus on one task only.
  Ex: A User class should handle only user related data, while db operations should be handled by a separate UserRepository class.
'''

class User:

  def __init__(self, name:str, age:int, email)-> None:
    self.name = name
    self.age = age
    self.email = email

  def get_user_info(self):
    print(f"This is {self.name} and my age is {self.age}")

  def is_adult(self)->bool:
    return self.age > 18