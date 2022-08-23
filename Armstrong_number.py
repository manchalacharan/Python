'''The given number is amstrong number'''
num = int(input("Enter a number is: "))
order = len(str(num))
s = 0
t = num

while t > 0:
    digit = t %10
    s +=digit**order
    t //=10

if num == s:
    print(num,"is Armstrong number.")
else:
    print(num,"is not an Armstrong number.")
