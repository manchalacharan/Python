''' the length of a month from 28 to 31days. the name of the month from user as a
string should display the number of days in that month.

Eg : input : January
     output : 31days '''

month = str(input("Enter a month Name: "))
a,b,c,d,e,f,g = 'jan','march','may','july','aug','oct','dec'
w,x,y,z = 'april','june','sep','nov'
A = 'feb'
if (month==a):
    print(month," is 31days")   
elif(month==A):
    print(month," is a 28 or 29days")
elif(month==b):
    print(month," is a 31days")
elif(month==w):
    print(month," is a 30days")
elif(month==c):
    print(month," is a 31days")
elif(month==x):
    print(month," is a 30days")
elif(month==d):
    print(month," is a 31days")
elif(month==e):
    print(month," is a 31days")
elif(month==y):
    print(month," is a 30days")
elif(month==f):
    print(month," is a 31days")
elif(month==z):
    print(month," is a 30days")
elif(month==g):
    print(month," is a 31days")
else:
    print("Error")
