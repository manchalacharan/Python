# Average

n = int(input("Enter a number: "))
sum1 = 0
count = 1
while(n !=0):
    sum1 = sum1 + n
    n = int(input("Enter another number: "))
    count = count + 1
    
avg = sum1/(count - 1)
print(avg)
