def myfunc(): #creating function
    print("Hello")

myfunc() #calling function

def namefunc(name): #passing arguments
    print("Hello " + name)
namefunc("Harivansh") #calling with arguments
namefunc("Maulik")

def my_function(*kids): #when number of arguments is unknown
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

def my_function(child3, child2, child1): #using keyword arguments
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
