''' the no.of.days form user & calculate the Charges for library

    Number of days     Charges
    --------------     -------
    Till 5 days        Rs 2/day
    6 to 10days        Rs 3/day
    11 to 15days       Rs 4/day
    After 15 days      Rs 5/day
'''

#amount = int(input("Enter your amount: "))
days = int(input("Enter days: "))

if(days<5):
    bill = days*2
    print("The Charges for library is: ",bill)
elif(days>=6 and days<=10):
    bill = days*3
    print("The Charges for library is: ",bill)

elif(days>=11 and days<=15):
    bill = days*3
    print("The Charges for library is: ",bill)
else:
    bill = days*3
    print("The Charges for library is: ",bill)
