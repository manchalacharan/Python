'''
Newton's method to computer display the square root of a number.
the algorithm of newton's method following
1. Read x form the user.
2. Initialize guess to x/2.
3. "While"guess to not good enough do.
4. Update to be the avaerage of guess and x/guess.
    guess contains an approximation of the square root of x.
    the  absolute value of the difference b/w guess*guess and x was less than or equal to 10e-12
'''
x = int(input("Enter the number: "))
guess = x/2

while ((guess**2)-(x)) >= 10e-12:
    guess = (guess + x/guess)/2
print("The square root of ",x,"is",guess)
