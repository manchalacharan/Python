''' Evaluate then valu of e**x upto 10 terms
    e**x = 1+ (x**1)/1!+ (x**2)/2! +(x**3)/3!+..............+(x**n)/n!
'''
x = int(input("Enter a x value: "))
n = int(input("Enter a no.of.terms: "))
ex = 0

for i in range(1,n):
    fact =1
    for j in range(1,i+1):
        fact=fact*j
    ex=ex+(x**i)/(fact)

print(ex+1)
    
