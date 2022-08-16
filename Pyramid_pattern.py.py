#Triangle method
#        Ex - 1(for loop)

n = int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print("*",end=" ")
    print("\r")

#         Ex - 2(while loop)

n = int(input())

i,j=1,0
while i<=n:
    while j<=i-1:
        print("*",end=" ")
        j+=1
    print("\r")
    j=0
    i=i+1

#        Ex - 3(while loop)

n = int(input())
i = 0

while i<=n:
    print(" "*(n-i)+"*"*i)
    i+=1

#       Ex - 4(for loop)

n = int(input())

for i in range(1,n+1):
    print(" "*(n-i)+"*"*i)

#       Ex - 5

n = int(input())
k = n-1

for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    k=k-1
    for j in range(0,i+1):
        print("*",end=" ")
    print("\r")

#      Ex - 6(numbers)

n = int(input())

for i in range(1,n+1):
    for j in range(1,i+1):
        print(n,end=" ")
        n+=1
    print("\r")

#      Ex - 7(Alphabets)

n = int(input())
num = 65
for i in range(1,n+1):
    for j in range(1,i+1):
        ch = chr(num)
        print(ch,end=" ")
        num+=1
    print("\r")
