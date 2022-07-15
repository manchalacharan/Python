'''Number of feet from the user follwed by a number of inches
    display the equivalent of centimeters
    Hint : one foot is 12 inches
           one inche is 2.54 centimeters'''

feet = float(input("Enter your feets: "))
inches = float(input("Enter your inches: "))

feet_cen = feet*12*2.54          
inches_cen = inches*2.54
hight_cen = feet_cen+inches_cen

print("Your hight in centimenters: ",hight_cen)
