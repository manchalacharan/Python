#The given number is convert list of below and above average 
n = input()
s = []
below_avg = []
above_avg = []

while n!="":
    num = int(n)
    s.append(num)
    n = input()

avg = sum(s)/len(s)
print("Average is: ",avg)

for i in s:
    if i<avg:
        below_avg.append(i)
    elif i>avg:
        above_avg.append(i)

print("Above average values are ",above_avg)
print("Below average values are ",below_avg)

