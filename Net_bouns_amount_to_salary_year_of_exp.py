''' A company gives bouns to employee

    Time period of service     Bouns
    ----------------------     -----
    More than 10 years          10%
    >=6 and <=10 years           8%
    Less than 6 years            5%

calcuate net bouns amount. '''

salary = float(input("Enter your salary amount: "))
exp = float(input("Enter your experiences: "))

if(exp>10):
    bouns = salary*0.1
    print("The net bouns amount is: ",bouns)
elif(exp>=6 and exp<=10):
    bouns = salary*0.08
    print("The net bouns amount is: ",bouns)
else:
    bouns = salary*0.05
    print("The net bouns amount is: ",bouns)
