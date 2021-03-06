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

def my_function(country = "Norway"): #providing default parameter value
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

def foodfunc(food): #passing list as an argument
    for x in food:
        print(x)
fruits = ["apple","mango","banana"]
foodfunc(fruits)

def f1(x):
    return 3*x #return keyword
print(f1(2))

def tri_recursion(k): #recursion implementation
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result
print("\nRecursion Example Results")
tri_recursion(6)
