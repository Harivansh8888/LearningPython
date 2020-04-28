import datetime

x = datetime.datetime.now() #working with date as object

y =datetime.datetime(2020, 5, 3) #creating a date object

print(x)
print(x.year) #prints current year
print(x.strftime("%A")) #prints the current day
