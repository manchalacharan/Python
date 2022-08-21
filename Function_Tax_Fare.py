'''
            Tax fare
            --------
Base fare is $4.00,plus $0.25
for every 140 meters travelled
'''
#Let us creat a function
def distance(d):
    meter = d*1000
    if (meter>140):
        price = 4 + ((meter/140)*0.25)
        print(price)
    else:
        print("Total fare is 4$")

#Let us ask user input
x = float(input("The distance travelled in km: "))

#Let us call the function
distance(x)
