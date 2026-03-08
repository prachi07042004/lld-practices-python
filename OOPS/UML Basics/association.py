'''UML(unified modeling language)-std way to visually design and represent software systems using diagrams
Importance:
Visualisation (blueprint), Documentation, Communication, Standarization

Class Diagrams: Class name then attribute names with their datatypes in one block then methods in next block
+ -> public   - -> private

Association: connection btw 2 or more classes that shows how their objects are related to each other. when one class's object uses or interacts with that of another class, that's association. "Class A knows about Class B and can use it"
To represent connect 2 classes boxes with arrow ->
'''

class Teacher:

  def __init__(self, name: str) -> None:
    self.__name:str = name

  def get_name(self) -> str:
    return self.__name
  
  def teach(self, student: "Student") -> None:
    print(f"{self.__name} is teaching {student.get_name()}")
  
class Student:

  def __init__(self, name:str) -> None:
    self.__name:str = name

  def get_name(self) -> str:
    return self.__name
  
teacher1 = Teacher("Sharma Sir")
student1 = Student("Prachi")

teacher1.teach(student1) #teach() takes student type as parameter

