'''The name of a shape from its numbers of side the support shapes with anywhere from 3 up to
(and include)6 sides. eg : input : 3
                            ouput : triangle '''

num = int(input("Enter a number: "))

if (num == 3):
    print("This is Triangle.")
elif(num == 4):
    print("This is Square.")
elif(num == 5):
    print("This is a Pentagonal.")
elif(num == 6):
    print("This is a Hexgonal.")
else:
    print("Error.")
