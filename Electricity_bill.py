''' To Calculate the electricity bill(accept no.of.units from user).
    uint               Price
    ----               -----
First 100units      Free of cost
Next 100 units      Rs 5 per unit
After 200 units     Rs 10 per unit

Eg: input : 350
    output : 2000 '''

units = int(input("Enter Units: "))

if(units<100):
    print("Free")
elif(units>=100 and units<=200):
    bill = 5*(units-100)
    print("Total amount is: ",bill)
else:
    bill = 10*(units-200)+5*100
    print("Total amount is: ",bill)
