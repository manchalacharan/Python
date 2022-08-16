#Revers order

n = int(input())
s=[]
s.append(n)

while n!=0:
    n = int(input())
    if n!=0:
        s.append(n)

print(s)
s.reverse()
print(s)
