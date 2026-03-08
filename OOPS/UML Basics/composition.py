'''
  Composition is strong "has-a" relationship where one class owns the objects of another class. If the container objects are destroyed, contained objects are destroyed automatically.
  "Class A owns Class B completely, If A dies, B also dies"
  Represented with filled diamond on the class which is containing(car)
  Ex: Car and engine

  Inheritance: "is-a" relationship where child class inherits properties and behavior of parent class 
  ex: child class is-a type of parent class 
  dog is a type of animal class
  empty triangle arrow pointing towards animal class
'''
class Engine:

  def __init__(self, engine_type, horsepower) -> None:
    self.__engine_type  = engine_type
    self.__horsepower = horsepower

  def get_details(self) -> str:
    return f"{self.__engine_type} Engine {self.__horsepower} HP"

  def start(self) -> None:
    print(f"{self.__engine_type} engine started!")

#Class Car (owns engine)- composition

class Car:

  def __init__(self, brand, model, engine_type, horsepower)-> None:
    self.__brand = brand
    self.__model = model

    #COMPOSITION : Engine is created inside car constructor
    #So basically when we are creating a car, we are creating an engine also inside it
    self.__engine = Engine(engine_type, horsepower)

  def get_car_details(self)-> None:
    print(f"\nCar: {self.__brand} {self.__model}")
    print(f"Engine: {self.__engine.get_details()}")

  def start_car(self) -> None:
    print(f"\nStarting {self.__brand} {self.__model}...")
    self.__engine.start()
    print("Car is ready to drive!")


#creating car object
my_car : Car = Car("Toyota", "Fortuner", "Diesel", 204)

#display car details
my_car.get_car_details()

#start the car
my_car.start_car()


#Important: when we delete the car, the engine is also destroyed!
del my_car

#we cannot access engine separately
#engine has no independent existance outside car

print("Car and engine both are destroyed")