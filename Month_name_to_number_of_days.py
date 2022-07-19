''' the length of a month from 28 to 31days. the name of the month from user as a
string should display the number of days in that month.

Eg : input : January
     output : 31days '''

month = str(input("Enter amonth Name: "))

if (month==january):
    print(month," is 31days")   
elif(month==february):
    print(month," is a 28 or 29days")
elif(month==march):
    print(month," is a 31days")
elif(month==april):
    print(month," is a 30days")
elif(month==may):
    print(month," is a 31days")
elif(month==june):
    print(month," is a 30days")
elif(month==july):
    print(month," is a 31days")
elif(month==august):
    print(month," is a 31days")
elif(month==september):
    print(month," is a 30days")
elif(month==october):
    print(month," is a 31days")
elif(month==november):
    print(month," is a 31days")
else:
    print(month," is a 31days")
