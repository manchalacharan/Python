# The given proper divisor of a postive integer values

n = int(input("Enter a number is: "))
s=[]

for i in range(1,n):
    if(n%i==0):
        s.append(i)

print(s)
