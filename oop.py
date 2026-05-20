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
