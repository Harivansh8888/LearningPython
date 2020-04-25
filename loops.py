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
