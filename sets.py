#sets have no index, they are unordered

set1 = {"abc","def","xyz"}
print(set1)

for x in set1:
    print(x) # unordered in printing

print("def" in set1) #returns True (boolean)

#set items can't be changed but we can add

set1.add("pqr") #adding an item
print(set1)

set1.update(["hello","world"]) #adding multiple items at once
print(set1)

print(len(set1)) #returns length of set

set1.remove("hello") #if item does not exist it will show error

set1.discard("pqr") #if item does not exist it will not show error

set1.pop() #sets are unordered so we don't know what will be removed

set2 = {"a","b","c"}
set2.clear() #empties the set

thisset = set(("hello","world")) #set() constructor
print(thisset)
#set2.del() #deletes the set permanently

s1 = {"1","2","3"}

s = set1.union(s1) #joining 2 lists
print(s)

set1.update(s1) #joining 2 lists
print(set1)
