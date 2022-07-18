"""
    The garde of a student based on marks
s.no     Marks        Grade
 1.     90 above      A - Excellent
 2.     70 above      B - Very Good
 3.     60 above      C - Good
 4.     40 above      D - Average
 5.     40 below      F - Failed
 """


Marks = int(input("Enter a Marks: "))

if(Marks > 90):
    print("A Grade")
elif(Marks > 70):
    print("B Grade")
elif(Marks > 60):
    print("C Grade")
elif(Marks > 40):
    print("D Grade")
else:
    print("Failed")
