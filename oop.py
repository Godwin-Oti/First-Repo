class MyClass:
    x=5
print(MyClass)

class MyClass:
    x=90
p1=MyClass()
print(p1.x)

class Person:
    def __init__(self,name, age):
       self.name=name
       self.age=age
p1=Person("John",30)
print(p1.name)
print(p1.age)

class Person:
    def __init__(self, name, age):
        self.name=name
        self.age=age
                                     
    def myfunc(self):                  #object method
        print("My name is "  + self.name)
p1=Person("John",40)
p1.myfunc()
        

class Person():
    def __init__(self, name, country, age):
        self.name=name
        self.country=country
        self.age=age
    
    def myfunc(self):
        print( " My name is " +self.name)
p1=Person("Oti","Nigeria",30)
p1.myfunc()

class Person:
    def __init__(oti,name,age):
        oti.name=name
        oti.age=age
    def agu(oti):
        print("My son name is " +oti.name + " and he  is ", 12)
p1=Person("Ben",14)
p1.agu()

class Person:
    def __init__(oti,name,age):
        oti.name=name
        oti.age=age
    def agu(oti):
        print("My son name is " +oti.name + " and he  is ", 12)
p1=Person("Ben",14)
p1.name="Darlington"
print(p1.name)
p1.agu()

##### INHERITANCE

class Person:
    def __init__(self,fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname,self.lastname)
x=Person("Oti","Ken")
x.printname()

class Father:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
class Son(Father):
    pass

x=Son("Oti", "Amaka")
x.printname()

class Person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self,fname, lname):
        Person.__init__(self,fname,lname)
p1=Student("Emma", "Odogwu")
p1.printname()
    
    

class Person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self,fname, lname):
        super().__init__(fname,lname)
p1=Student("Emma", "Odogwu")
p1.printname()


class Person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self,fname, lname):
        super().__init__(fname,lname)
        self.graduationyear=2012
p1=Student("Emma", "Odogwu")
print(p1.graduationyear)




class Person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self,fname, lname,year):
        super().__init__(fname,lname)
        self.graduationyear=year
p1=Student("Emma", "Odogwu",2012)
print(p1.graduationyear)


class Person:
    def __init__(self,fname,lname):
        self.firstname=fname
        self.lastname=lname
    def printname(self):
        print(self.firstname, self.lastname)
class Student(Person):
    def __init__(self,fname,lname, year):
        super().__init__(fname,lname)
        self.graduationyear=year
    def welcome(self):
        print("My name is ",self.firstname, self.lastname, "I graduated in the year ", self.graduationyear) 
p1=Student("Godwin","Oti",2018)
p1.welcome()



class Car:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Drive!")
class Boat:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self): 
        print("Sail!")
class Plane:
    def __init__(self, brand, model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Fly!")
car1=Car("Mercedez",4567)
boat1=Boat("Warship", 236)
plane1=Plane("Boeing", 36)
for x in (car1,boat1,plane1):    
    x.move()


    
    

class Vehicle:
    def __init__(self,brand,model):
        self.brand=brand
        self.model=model
    def move(self):
        print("Move!")
class Car(Vehicle):
    pass
class Boat(Vehicle):
    def move(self):
        print("Sail!")
class Plane(Vehicle):
    def move(self):
        print("Fly!")
car1=Car("Ford", "Explorer")
boat1=Boat("Titanic","Dreams")
plane1=Plane("Boeing","Flamingo")
for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    
    x.move()
