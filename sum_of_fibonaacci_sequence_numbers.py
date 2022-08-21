# Then sum of the fibonaacci sequence number 

n = int(input("Enter a n Value: "))

a = 0
b = 1

while (0<n):
    print(a)
    x = a+b
    a=b
    b=x
    n = n-1

