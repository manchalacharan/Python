'''the cost of meals ordered a restaurant from the user
    computing 18% of tax and tip
the grand totalfor meal including both tax and the tip.'''

price = int(input("Enter a amount : "))

#tax1 = float(input("Enter the tax percentage: "))         #you can choose tax
#tip1 = float(input("Enter the tip percentage: "))         #you can choose tip
tax = price*0.18
tip = price*0.18

total = price + tax +tip

print("Toatal amount is: ",total)
