class MyClass: #creating a class
    x=5

p1 = MyClass() #creating an object of MyClass
print(p1.x)

class Person:
    def __init__(self, name, age): #__init__() function is automatically called everytime when class is used to create a new object
        self.name = name
        self.age = age #the self parameter is a reference to the current instance of the class
    
    def myfunc(self):
        print("Hello my name is " + self.name)


p1 =Person("Harivansh", 19)
print(p1.name)
print(p1.age)


p2 = Person("Maulik", 20)
p2.myfunc()

class Food:
    def __init__(harivansh, dish, quantity): #self parameter can be named anything
        harivansh.dish = dish
        harivansh.quantity = quantity

p3 =Food("Pav Bhaji", 2)
print(p3.dish)
print(p3.quantity)

p3.quantity = 4 #modifying object properties

print(p3.dish)
print(p3.quantity)
