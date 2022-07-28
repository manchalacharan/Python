'''marks using dicitinoary datatype '''

marks = {"eng" : 60, "hin" : 75, "math" : 85, "phy" : 65, "che" : 65}
roll = [10,25,36,42,50]  
# loop to sum all values 
dic = 0
lis = 0
for i in marks.values():
    dic += i

for j in roll:
    lis += i
  
# using len() to get total keys for mean computation
dic = dic / len(marks)
lis = sum(roll)/len(roll)

# printing result 
print("The computed mean : " + str(dic))
print("The computed mean : " + str(lis))

"""
marks = {"eng" : 60, "hin" : 75, "math" : 85, "phy" : 65, "che" : 65}

count = sum(marks.values())/len(marks) 
print("The computed mean : " + str(count))
"""
