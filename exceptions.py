try:
    print(x) #x is not defined here
except:
    print("An exception occured")

try:
    print(y)
except NameError:
    print("y is not defined") #many exceptions with a single try
except:
    print("Some other exception occured")