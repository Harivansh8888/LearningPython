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
