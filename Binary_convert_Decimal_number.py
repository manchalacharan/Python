''' Binary to Decimal convert '''

bin_num = input("Binary number is: ")
x = 0
j = 0

for i in range(len(bin_num)-1,-1,-1):
    a= (2**j)*int(bin_num[i])
    x+=a
    j+=1  

print("The binary convert decimal is: ",x)
