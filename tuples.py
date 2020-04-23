name = ("harivansh","neha","maulik") #making a tuple

print(name) #printing a tuple

print(name[1]) #accessing a tuple item

print(name[-1]) #accessing item by negative indexing

print(name[0:2]) #range of indexes, 2 is excluded here

print(name[-3:-1]) #range of negative indexes, -1 is excluded here

x = ("apple", "banana", "cherry") #tuple is unchangeable
y =list(x) #converting tuple into list
y[1] = "mango" #changing item in list
x = tuple(y) #converting list back to tuple
print(x)
