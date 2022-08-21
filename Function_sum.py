'''
sum of the n postive integer
        a**2 + b**2 = c**2
                (or)
        s = n*(n+1)/2
'''
#Create  a function
def sum_n(n):
    s = n*(n+1)/2
    print(s)
#user input
x=int(input())
#Call the function 
sum_n(x)
