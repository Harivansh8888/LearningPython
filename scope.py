def myfunc():
  x = 300 #x can only be used inside myfunc() because it is declared inside the function ---> scope
  print(x)

myfunc()

def func1():
    y = 200
    def innerfunc():
        print(y) #function inside a function so x can be used 
    innerfunc()
func1()

z = 10 #global scope ---> declared outside the function

def func2():
    print(z)

func2()

print(z)

a = 500  
def fun(): # both a are considered diff variables here
    a= 700
    print(a)

fun()

print(a)

b = 400 
def fun1(): #
    global b
    b = 23 #global keyword will change the value of 400 to 23

fun1()

print(b)
