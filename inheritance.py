class Person: #parent class
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname
  def printname(self):
    print(self.firstname, self.lastname)
x = Person("Harivansh", "Mathur")
x.printname()

class Student(Person): #creating a subclass or child class
    print("Hi from the child class")
x = Student("Neha", "Singh")
x.printname()

#__init__() function can be used in child class
#when you add the __init__() function, the child class will no longer inherit the parent's __init__() function
#the child's __init__() function overrides the inheritance of the parent's __init__() function

class Stu(Person): #creating another child class
  def __init__(self, fname, lname):
    Person.__init__(self, fname, lname) #to keep the inheritance of the parent's __init__() function
