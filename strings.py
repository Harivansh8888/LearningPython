print("Hello")
print('World')

a = "Harivansh"
print(a)

b = 'Mathur'
print(b) 

c = """My name is Harivansh
I am currently in Kanpur
Stay Home"""
print(c)  #Multiline Strings

d = '''Hey Everyone
I hope you are having a good day'''
print(d) #Multiline Strings

e = 'Hello World'
print(e[4])  #Strings are Arrays in Python

f = 'Hello World'
print(f[2:5]) #Slicing the String

g = 'Hello World'
print(g[-5:-2]) #Slicing starts from ending-Negative Indexing

h = "  Harivansh Mathur    "
print(h.strip())  #Removing whitespaces from beginning and end

age = 19
lang = 3
o = "My name is Harivansh and I am {} and i know {} languages"
print(o.format(age,lang)) #Combinig String and Integer

i = 'Harivansh'
print(i.lower()) #Convert to Lower case

j = 'Mathur'
print(j.upper()) #Convert to Upper case

k = "Kanpur"
print(k.replace("K","B")) #Will print Banpur

l = "Hello,Everyone"
print(l.split(",")) #returns array of 2 strings- Hello and Everyone

m = "My name is X"
txt = "name" in m
print(txt) #returns boolean value - true if found and vice versa

n1 = 'Hello'
n2 = 'World'
n3 = n1 + " " + n2
print(n3) #String Concatenation

age = 19
lang = 3
o = "My name is Harivansh and I am {} and i know {} languages"
print(o.format(age,lang)) #Combinig String and Integer

p = "My country is \"India\" and I am a pround Indian"
print(p) #Escape character for showing double quotes in a string
