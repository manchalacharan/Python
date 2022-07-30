''' String Palindrome to identical forward and backward
    "anna","civic","level" and "hannah" is a palindrome words.   '''
name = str(input("Enter a Name: ",))

rstr = name[::-1]

if name == rstr:
    print("This is a Palindrome")
else:
    print("This is not a Plaindrome")
