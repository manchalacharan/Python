''' To convert any number in b\w 1to9 to it Roman number'''

num = int(input("Enter a number: "))

#I,V,X,L,C,D,M = 1,5,10,50,100,500,1000

if(num == 1):
    print("I")
elif(num == 2):
    print("II")
elif(num == 3):
    print("III")
elif(num == 4):
    print("IV")
elif(num == 5):
    print("V")
elif(num == 6):
    print("VI")
elif(num == 7):
    print("VII")
elif(num == 8):
    print("VIII")
elif(num == 9):
    print("IX")
else:
    print("Error")
