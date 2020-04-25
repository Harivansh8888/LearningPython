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
