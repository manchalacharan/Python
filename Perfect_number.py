# The given number is perfect number

n = int(input("Enter a numnber is: "))
sum1 = 0

for i in range(1,n):
    if (n%i == 0):
        sum1 +=i

if (sum1 == n):
    print(n,"This is Perfect number.")
else:
    print(n,"This is not a Perfect number.")

'''             or
                --
x = int(input("Enter a first number: "))
y = int(input("Enter last number: "))

for i in range(x,y-1):
    sum1 = 0
    for j in range(1,i-1):
        if (i%j == 0):
            sum1 += j
    if sum1 == i:
        print(i)
'''

