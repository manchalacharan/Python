''' Prime factor '''

n = int(input("Enter a number is: "))   # Prime factor of a integer number n
fact = 2                                # Then factor is equal to 2

while(fact <= n):                       # Factor is less then or equal to n
    if (n%fact == 0):                   # If n is evenly dvisible by factor     
        print(fact,end="*")                     
        n = n//fact                     # Divide n by factor using floor divison
    else:
        fact = fact + 1                       # Increase factor by 1
    
