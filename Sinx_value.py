''' Evaluate then valu of e**x upto 10 terms
    sinx = x - x**3/3! + x**3/3! -...........(-1)**k . x**(2k+1)/(2k+1)!=[
'''
x = int(input("Enter a x value: "))
n = int(input("Enter a no.of.terms: "))
sin_x = 0

for k in range(1,n):
    fact =1
    for j in range(1,k
                   +1):
        fact=fact*j
    sin_x = (-1**k)*x**(2*k+1)/(2*k+1)*(fact)

print(sin_x)
