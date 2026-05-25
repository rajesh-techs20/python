DAY 1

#creating class 
class student:
  name="Rajesh G R"
#creating objects 
s1=student()
  print(s1.name)

class car:
  color="black"
  brand="mercedes"
#this is objects
car1=car()#constructor
print(car1.color)
print(car1.brand)
#output 


#__init__ Function
#creating class
class student:
  def __init__(self,fullname):
  self.name=fullname
#self parameter is a reference to the current instance of the class and is used to access variables that belongs to the class
#creating object
s1=student("rajesh")
print(s1.name)

DAY 2
#another example
class student:
  def __init__(self,name,age):
    self.name=name
    self.age=age
s1=student("Rajesh",19)
print(s1.name)
print(s1.age)
#output
Rajesh
18

#example 3 
class mobile:
  def __init__(self,brand,price):
    self.name=brand
    self.cost=price
m1=mobile("VivoY30",15000)
print(m1.name)
print(m2.cost)

#output
VivoY30
15000

#function inside class
class student:
  def __init__(self,name):
    self.name=name
  def greet(self):
    print("Hello",self.name)
  s1=student("Rajesh")
  s1.greet()

#creating multiple objects
class student:
  def __init__(self,name):
    self.name=name
s1.student("Rajesh")
s2=student("Ramu")
print(s1.name)
print(s2.name)

#output
Rajesh 
Ramu

#Task  1
#create a car class with brand model and print details

class car:
  def __init__(self,brand,model):
    self.brand=brand
    self.model=model
  def details(self):
    print("Brand:",self.brand)
    print("Model:",self.model)
  car1=car("Ambassidor",1943)
  car2=car("BMW",2009)
  car1.details()
  car2.details()

#output
Brand:Ambassidor
Model:1943
Brand:BMW
Model:2009

#Task2
#create a class of dogs with name and age and add bark() method ....Output be Tommy is barking
class dog:
  def __init__(self,name,age):
    self.name=name
    self.age=age
  def bark(self):
    print(self.name,"is barking")
d1=dog("Tommy",6)
d1.bark()

#task 3 
#create a class of employees to store their details 
class employee:
  def __init__(self,name,age,salary):
    self.name=name
    self.age=age
    self.salary=salary
  def details(self):
    print("Name:",self.name)
    print("Age:",self.age)
    print("Salary:",self.salary)
e1=employee("Arun",24,45000)
e2=employee("Chethan",21,40000)
e1.details()
e2.details()

#Output 
Name: Arun
Age: 24
Salary: 45000

Name: Chethan
Age: 21
Salary: 40000

#Inheritence in class 

class Animal:
  def soud(self):
    print("Animals make sound")
class dog(Animal):
  pass
d1=Dog()
d1.sound()

# =========================================
# INHERITANCE IN PYTHON - PRACTICE PROGRAMS
# =========================================


# =========================================
# PROGRAM 1
# Question:
# Create a class Vehicle with info() method.
# Create child class Car and inherit Vehicle class.
# =========================================

class Vehicle:

    def info(self):
        print("This is a vehicle")


class Car(Vehicle):
    pass


car1 = Car()

car1.info()



# =========================================
# PROGRAM 2
# Question:
# Create a class Animal using eat() method.
# Create child class Cat using sound() method.
# Call both methods using one object.
# =========================================

class Animal:

    def eat(self):
        print("Animal is eating")


class Cat(Animal):

    def sound(self):
        print("Cat says meow")


cat1 = Cat()

cat1.eat()
cat1.sound()



# =========================================
# PROGRAM 3
# Question:
# Create a class Person with constructor
# storing name and age.
# Create child class Teacher using super().
# Store subject and print details.
# =========================================

class Person:

    def __init__(self, name, age):
        self.name = name
        self.age = age


class Teacher(Person):

    def __init__(self, name, age, subject):

        super().__init__(name, age)

        self.subject = subject

    def details(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Subject:", self.subject)


teacher1 = Teacher("Arun", 35, "Physics")

teacher1.details()



# =========================================
# PROGRAM 4
# Question:
# Create class Vehicle with start() method.
# Create child class Bike with ride() method.
# Call both methods.
# =========================================

class Vehicle:

    def start(self):
        print("Vehicle started")


class Bike(Vehicle):

    def ride(self):
        print("Bike is riding")


bike1 = Bike()

bike1.start()
bike1.ride()



# =========================================
# POLYMORPHISM / METHOD OVERRIDING
# =========================================


# =========================================
# PROGRAM 5
# Question:
# Create parent class Animal with sound().
# Override sound() in child class Dog.
# =========================================

class Animal:

    def sound(self):
        print("Animal makes sound")


class Dog(Animal):

    def sound(self):
        print("Dog barks")


d1 = Dog()

d1.sound()



# =========================================
# PROGRAM 6
# Question:
# Create class Bird with speak() method.
# Override speak() in child class Parrot.
# =========================================

class Bird:

    def speak(self):
        print("Bird makes sound")


class Parrot(Bird):

    def speak(self):
        print("Parrot talks")


p1 = Parrot()

p1.speak()



# =========================================
# PROGRAM 7
# Question:
# Create class Shape with draw() method.
# Override draw() in child class Circle.
# =========================================

class Shape:

    def draw(self):
        print("Drawing shape")


class Circle(Shape):

    def draw(self):
        print("Drawing circle")


c1 = Circle()

c1.draw()

#REVISION
class Employee:
  def __init__(self,name,salary):
    self.name=name
    self.salary=salary
  def show(self):
    print("Name:",self.name)
    print("Salary:",self.salary)
class Manager(Employee):
  def __init__(self,name,salary,department):
    super().__init__(name,salary):
    self.department=department
  def show(self):
    print("Manager Name:",self.name)
    print("Salary:",self.salary)
    print("Department:",self.department)
man1=Manager("Arun",50000,"HR")
man1.show()

#TASK 2
class Animals:
  def sound(self):
    print("Animals make sound ")
class Dog(Animals):
  def bark(self):
    print("Dog Barks")
class Cat(Animals):
  def meow(self):
    print("Cat Meows")
dog1=Dog()
cat1=Cat()
dog1.sound()
cat1.sound()

ENCAPSULATION : HIDING DATA FROM DIRECT ACCESS 
eg : ATM hides bank details , mobile hides internal systems

Private variable example 
class bank:
  def __init__(self,balance):
    self.balance=balance
b1= Bank(50000)
print(b1.__balance)

OUTPUT:
Attribute Error

Access using method
class Bank:
  def __init__(self,balance):
    self.balance=balance
  def showBalance(self):
    print("Balance:",self.__balance)
  b1=Bank(50000)
  b1.showBalance()

Output 
Balance: 50000

TO PROTECT DATA 
TO PROVIDE SECURITY TO DATA WE USE ENCAPULATION

class Student:
  def __init__(self,marks):
    self.marks=marks
  def display(self):
    print("MArks:",self.__marks)
s1=Student(95)
s1.display()

#Task !
class Account:
  def __init__(self,password):
    self.__password=password
  def show_password(self):
    print("Password is displayed",self.__password)
a1=Account(1234)
a1.show_password()

#Task 2
class Mobile:
  def __init__(self,price):
    self.__price=price
  def show_price(self):
    Print("Price:",self.__price)
m1=Mobile(50000)
s1.show_price()

class student:
  def __init__(self,marks):
    self.__marks=marks
  def showmarks():
    print("Marks",self.__marks)
s1=students(97)
s1.showmarks()

#Abstraction
Hiding implementation details
real life examples
ATM Machine
Car driving
Mobile Apps

Example 
from abc import ABC,abstractmethod;
class Vehicle(ABC):
  @abstractmethod 
  def start(self):
    pass 
class Bike(Vehicle):
  def start(self):
    print("Bike started")
b1= Bike()
b1.start()

Output 
Bike started


Another Example:
from abc import ABC,abstractmethod
class Animal(ABC):
  @abstractmethod
  def sound(self):
    pass
class Dog(Animal):
  def sound(self):
    print("Dog Barks")
d1=Dog()
d1.sound()

Task 1 :
from abc import ABC,abstractmethod
class Shape(ABC):
  @abstractmethod
  def draw(self):
    pass
class Circle(Shape):
  def draw(self):
    print("Drawing Circle")
c1=Circle()
c1.draw()


