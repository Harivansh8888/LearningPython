#while loops --->

i = 1
while i < 6:
  print(i) #six won't be printed
  i += 1 #increasing i value by one

i = 1
while i < 6:
  print(i) #will only print 1,2,3
  if i == 3:
    break
  i += 1

i = 0
while i < 6:
  i += 1
  if i == 3: #this will not print 3 
    continue
  print(i)

i = 1
while i < 6:
  print(i)
  i += 1
else: #else with while
  print("i is no longer less than 6")

#for loops --->

fruits = ["apple", "banana", "cherry"] 
for x in fruits: #looping through a list
  print(x)

for x in "banana":
  print(x) #looping through a string

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana": #will exit loop when banana is found
    break

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break  #banana won't be printed and loop exited
  print(x)
  
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue #banana won't be printed but loop will continue
  print(x)

for x in range(6): #default start by 0 and default increment by 1 each time
  print(x) #excludes 6

for x in range(2, 6): #prints 2,3,4,5
  print(x)

for x in range(2, 30, 3): #increment of 3 each time between 2 and 30
  print(x)

for x in range(6):
  print(x)
else: #else with for loop
  print("Finally finished!")
  
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj: #nested for loops
  for y in fruits:
    print(x, y)

for x in [0, 1, 2]:
  pass #pass statement when no content to provide
