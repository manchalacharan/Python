# Checking for prime number

num = int(input("Enter number: "))

if num>1:
    for i in range(2,num//2):
        if (num%i)==0:
            print(num,"is not a prime number")
            print(i,"*",num//i,"=",num)
            break
    else:
        print(num,"is a prime number")

