# it is a collection
#unordered, changable, indexed
# have keys and value

dict1 = {
    "brand": "BMW",
    "model": "i8",
    "year": "2020"
}

print(dict1)

x =dict1["model"] #alternative --> x=dict1.get("model")
print(x)  #x will store i8(value) here

dict1["year"] = "2018" #changing valuess
print(dict1)

for x in dict1:
    print(x) #prints the keys

for x in dict1:
    print(dict1[x]) #prints values

for x in dict1.values():
    print(x) #prints values

for x,y in dict1.items():
    print(x,y) #prints keys and values

if "year" in dict1: #checking if key exists
    print("Yes") 

print(len(dict1)) #prints length of dictionary

dict1["color"] = "blue" #adding item
print(dict1)

dict1.pop("year") #removing item
print(dict1)

mydict = dict1.copy() #copying dictionary
print(mydict)

myfamily = { #nested dictionaries
  "child1" : {
    "name" : "Rahul",
    "year" : 2004
  },
  "child2" : {
    "name" : "Rohan",
    "year" : 2007
  },
  "child3" : {
    "name" : "Raj",
    "year" : 2011
  }
}
print(myfamily)
