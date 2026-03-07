class Student:

  #Methods
  def __init__(self, name: str, age: int, gender: str) -> None:
    #Attributes
    print("This is a constructor/initializer")
    self.name = name
    self.age = age
    self.gender = gender

  def display(self) -> None:
    print(f"My name is {self.name}, age is {self.age} and gender is {self.gender}")

  def get_age(self) -> int:
    return self.age

s1 = Student("Pulkit", 26, "Male")
print(s1.get_age()) #if a method is returning smthing, use print to get the output displayed

s2 = Student("Prachi", 21, "Female")

