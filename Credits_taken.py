'''User take how many credits they have taken.

1. Freshman taken 23 or less
2. Sophamore taken b/w 24 and 53.
3. Juniors is taken b/w 54 to 83.
4. seniors is taken b/w 84 and over. '''

credit = int(input("Enter how amny credits is taken: "))

if(credit <= 23):
    print("The student is a fresher.")
elif(credit >= 24 and credit <= 53):
    print("They are a sophamore.")
elif(credit >= 54 and credit <= 83):
    print("They are Juniors.")
else:
    print("They are Seniors.")
