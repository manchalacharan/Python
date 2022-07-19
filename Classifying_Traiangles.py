''' A triangle has three side
--> A Equilateral triangle is all side are equal.
--> A Isosceles triangle is three side are unequal.
--> A Scalene triangle is two side is equal another on side is different.'''

x = int(input("Enter X value: "))
y = int(input("Enter y value: "))
z = int(input("Enter z value: "))

if(x==y==z):
    print("This is Equilateral Triangle.")
elif(x==y or y==z or z==x):
    print("This is Isosceles Triangle.")
else:
    print("This is Scalene Triangle.")
