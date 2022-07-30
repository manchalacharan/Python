""" Multiple word palindromes when spacing is ignored
eg:'go dog','flee to me remote elf','some men interpret nine memos'
and check whether or not a string is a palindrome.for additional challenage
that also ignore punctuation marks and treats uppercase and lowercase letter as equivalent"""

name = input("Enter a name is:")
n1 = name.lower()
na = n1.replace(" ","")
print(na,"\n")

rstr = na[::-1]
print(rstr)
if  na== rstr:
    print("This ia Palindrome.")
else:
    print("This is not Palindrome")
