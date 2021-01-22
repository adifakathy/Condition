#if....elif...else conditions
from typing import List

a = int(input("enter 1st value:"))
b = int(input("enter 2nd value:"))
if a > b :
    print("1st value is greater than 2nd value")
elif b > a:
    print("2nd value  is greater than 1st value")
else:
    print("both are equal")

#short hand if...else conditions
print("Mango") if a > b else print("lichi")
'''Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b
we can use "and" & "or" in condition
'''
#While conditions
i = 0
while i <= 20:
 print(i)
 i = i+1
 if(i==10):
     # we can also use break insted of continue
     continue
print("program end")
#we can also use else: condition
#for loop
fruits = ["apple","banana","cherry"]
for x in fruits:
    print(x)
for x in "banana":
    print(x)
#use of break condition
fruits = ["dalia", "rose", "lili"]
for x in fruits:
  print(x)
  if x == "rose":
    break
#we also use continue condition as before if condition and then use print

#range() Function
for x in range(10):
    print(x)
# We can also use limit like(2,10)
#Nested loops using for loop
adj = ["red","blue","black"]
fruits = ["rose","Berry","Brush"]
for x in adj:
    for y in fruits:
        print(x,y)






