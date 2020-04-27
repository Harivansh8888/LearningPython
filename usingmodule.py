import mymodule #importing all the data from the mymodule.py

mymodule.greeting(" Harivansh") #accessing that function

a = mymodule.person1["country"] #accessing dictionary created in mymodule.py
print(a)

"""
import mymodule as mx -----> to rename a module
a = mx.person1["age"]
"""
import platform #built in module in python

x = platform.system()
print(x)

y = dir(platform) #listing all the names defined in platform module
print(y)

z = dir(mymodule)
print(z)

# from mymodule import greeting -----> to only import a particular part of the module
