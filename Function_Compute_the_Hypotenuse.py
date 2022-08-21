'''
using Hypotenuse formula
    C**2 = A**2 + B**2
'''
#Create a function
def hypo(a,b):
    c = (a**2 + b**2)**0.5
    print(c)
#user inputs
x = int(input("Enter a first value is: "))
y = int(input("Enter a second value is: "))
#call the function
hypo(x,y)
