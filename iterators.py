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
