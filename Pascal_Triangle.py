'''         Pascal's triangle
            -----------------
            1
           1 1
          1 2 1
         1 3 3 1
        1 4 6 4 1
'''
n = int(input("Enter a number is: "))

for i in range(1,n+1):
    for j in range(0,n-i+1):
        print(' ',end='')

    c = 1
    for j in range(1,i+1):
        print(' ',c,sep = '',end = '')
        c = c * (i-j)//j
    print()
