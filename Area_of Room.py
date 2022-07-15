''' User to Enter width and length and program will display the Area of room
    then length and width will enter of a floating point number.
    include units your prompt and output message: either feets (or) meeter
    Eg : length = 10f(or)m
         width = 12f(or)m
         output = 120 (f(or)m)^2''' 

length = float(input("Length="))
width = float(input("Width="))

area = length * width

print("Area of a room : ",area)
