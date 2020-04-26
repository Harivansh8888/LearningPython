#lambda is a special/different type of function

x = lambda a,b: a*b*10 #can take multiple arguments
print(x(2,3))

def myfunc(n):  
    return lambda a: a*n 
mydoubler = (myfunc(2)) #using as an ananymous function inside other function
print(mydoubler)
