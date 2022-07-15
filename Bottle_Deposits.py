'''Small deposit is add drink containers to encourage people to recycle them
    Drink container holding one liter or less have a $0.10 deposit
    Drink container holding more then one liter or less have a $0.10 deposit
Program should continue by computing and display the refund that will be received
for returning those containers'''

bottle_above_liter = int(input("Enter the no of bottle(above it): "))
bottle_below_liter = int(input("Enter the no of bottle(below it): "))

refund = (bottle_above_liter*0.25)+(bottle_below_liter*0.1)

print("The total refund value = ",refund)

