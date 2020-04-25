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
