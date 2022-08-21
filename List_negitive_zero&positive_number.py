# List of the given negatives,zero and positives
                    
line = input ("Enter an integer(blank to quit):")
negatives   = []
zeros  = []
positives   = []

while line   !=  "":
   num = int (line)
   if  num   <  0:
      negatives.append(num)
   elif num   >  0:
      positives.append(num)
   else :
      zeros.append(num)

   # Read the next line of input from the user
   line = input ("Enter an integer(blank to quit):")

# Display all of the negative values, 
# then all of the zeros, then all of the positive values
print ("The numbers were:")
#for   n  in  negatives:
print (negatives)
#for   n  in  zeros:
print (zeros)
#for   n  in  positives:
print (positives)

'''#                           OR
#                              --

n = input()
s=[]

while n!="":
    num = int(n)
    s.append(num)
    n = input()
    s.sort()

print(s)
'''
