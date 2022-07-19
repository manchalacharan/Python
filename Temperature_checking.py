''' To enter temperature in Celsius
1. Temperature lee than -273.15 is invalid.
2. Temperature Exactly -273.15 is absolute 0.
3. Temperature is b/w -273.15 to 0 is freezing.
4. Temperature is 0 is freezing point.
5. Temperature is b/w 0 to 100 is normal range.
6. Temperature is 100 is boiling point.
7. temperature is a above 100 is above the boiling point. '''

c = float(input("Enter a Temperature in celsius is: "))

if(c < -273.15):
    print("Temperature is invalid")
elif(c == -273.15):
    print("Temperature is absolute 0")
elif(c >= -273.15 and c < 0):
    print("Temperature is below freezing")
elif(c == 0):
    print("Temperature is freezing point")
elif(c >= 0 and c < 100):
    print("Tepmerature is normal range")
elif(c == 100):
    print("Temperature is boiling point")
else:
    print("Temperature is above the boiling point")
    
