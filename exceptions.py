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

try:
    print("Hello")
except:
    print("Some error occured")
else:
    print("Nothing gets wrong") #using else with try and except

try:
    print(x)
except:
    print("Something is wrong")
finally: #it will run regardless of exception occurence
    print("try-except is executed")
