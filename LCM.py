''' Least common multiple '''

a = int(input("Enter first number is: "))
b = int(input("Enter second number is :"))

if a>b:
    i = a
else:
    i = b
while(True):
    if(i%a==0 and i%b==0):
        print(i)
        break
    i = i + 1 

print("The Least common multiple number is: ",i)
