list1 = ["apple","mango","pineapple"] #making a list
print(list1) # printing list

print(list1[2]) #accessing an item from list

print(list1[-1]) #accessing by negative indexing

list2 = ["harivansh","maulik","hridyanshu","ingit","jatin","neha","harshil"]
print(list2[2:5]) #range of indexes [a:b]- a included, b not included 

print(list2[:3]) #prints from beginning to specified index

print(list2[3:]) #prints from specified index to end

print(list2[-4:-1]) #range of negative indexes

list3 = ["dehradun","kanpur","jaipur","new delhi"]
list3[0] = "mumbai" #changing item value
print(list3) #printing updated list

list4 = ["mathur","singh","sharma","chhabra"]
for x in list4:  #looping through a list
    print(x)
if "singh" in list4: #checking if item exists in list
    print("Present")
else:
    print("Absent")

print(len(list4)) #prints length of list

list4.append("singhal") #adding items to the list
print(list4)

list4.insert(2,"uppal") #inserting new item at specified index, rest all will be shifted
print(list4)
