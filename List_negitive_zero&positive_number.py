# List of the given negatives,zero and positives

n = input()
s=[]

while n!="":
    num = int(n)
    s.append(num)
    n = input()
    s.sort()
        
print(s)
