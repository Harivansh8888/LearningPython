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
