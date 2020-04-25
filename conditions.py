a = 33
b = 200
if b > a: #if implementation
  print("b is greater than a")

p = 10
q = 10
if p > q: #if and elif implementation
    print("p is greater than q")
elif p == q:
    print("p and q are equal")

c = 10
d = 13
if c > d: #if, elif and else implementation
    print("c is greater than d")
elif c == d:
    print("c and d are equal")
else:
    print("d is greater than c")

if b > a: print("Yes") #shorthand for if

a = 2
b = 330
print("A") if a > b else print("B") #shorthand for if-else

a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B") #shorthand for multiple if-else

a = 200
b = 33
c = 500
if a > b and c > a: #AND condtion
  print("Both conditions are True")

a = 200
b = 33
c = 500
if a > b or a > c: #OR condition
  print("At least one of the conditions is True")
