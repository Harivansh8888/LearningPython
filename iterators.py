mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

#An iterator is an object that contains a countable number of values
#An iterator is an object that can be iterated upon, meaning that you can traverse through all the values
#consist of the methods __iter__() and __next__()

mystr = "banana" #strings are also iterable objects
myit1 = iter(mystr)

print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))

for x in mytuple: #iterating using for loop
    print(x)

class MyNumbers: #creating an iterator using __iter__() and __next__() methods
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter)) #if here we use for loop for printing it would go on forever
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))
print(next(myiter))

class MyNum:
    def __iter__(self):
        self.a = 1
        return self
    
    def __next__(self):
        if self.a <=20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration #using StopIteration so that for loop doesn't run forever

myclass1 = MyNum()
myiter1 = iter(myclass1)

for x in myiter1:
    print(x)
