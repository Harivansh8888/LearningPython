print(20 > 45) #returns boolean value
print(19 == 19)

a = 20
b = 30

if b > a: #if else working
    print('Wow')
else:
    print('Hey')

print(bool("Hello")) #returns true
print(bool(1)) #returns true
print(bool(0)) #returns false

def myFunction(): #function can return boolean
    return True  

if myFunction():
    print("YES!")
else:
    print("NO!")

x = 43
print(isinstance(x,int)) #returns true bcoz 43 is an integer
