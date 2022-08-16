#list mainplate
'''n = int(input())
s = []

for i in range(0,n+1):
    if n!=0:
        n = int(input())
        n.append(n)
        i=i+1

print(s.sort())
'''

n = int(input())
s=[]
s.append(n)

while n!=0:
    n = int(input())
    if n!=0:
        s.append(n)

print(s)
s1 = sorted(s)
print(s1)

