''' 
  Aggregation is a weak "has - a" relationship where one class contains objects of another class , but the contained objects can survive independently even if the container is destroyed. "Class A has Class B, but B can exist without A"
  ex: department class has student class but student class is independent
  Classes interaction represented with a line with an empty diamond on the side which is containing and line on the side which is being contained(student class)
'''

from typing import List

#Student class can exist independently
class Student:
  def __init__(self, name:str, roll_no:int) -> None:
    self.__name = name
    self.__roll_no = roll_no

  def get_name(self) -> str:
    return self.__name
  
  def get_roll_no(self) -> int:
    return self.__roll_no
  
#Department class contains Students- Aggregation
class Department:
  def __init__(self, dept_name:str) -> None:
    self.__dept_name:str = dept_name
    self.__students: List[Student] = []

  def add_student(self, student: Student)->None:
    self.__students.append(student)

  def show_students(self) -> None:
    print(f"Students in {self.__dept_name} department:")
    for student in self.__students:
      print(f"- {student.get_name()} (Roll No: {student.get_roll_no()})")

#creating student objects(they exist independently)
student1: Student = Student("Rahul", 101)
student2: Student = Student("Sneha", 102)
student3: Student = Student("Vanshika", 103)

#Creating dept object
cs_dept: Department = Department("Computer Science")

#adding students to department (aggregation happening here)
cs_dept.add_student(student1)
cs_dept.add_student(student2)
cs_dept.add_student(student3)

#display students
cs_dept.show_students()

#!!Even if we delete dept, students still exist
del cs_dept

#students are still aliva and can be used
print(f"\n Student still exist: {student1.get_name()}")