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
