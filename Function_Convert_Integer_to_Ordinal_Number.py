#       integer to string
def num(a):
    list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
    list2 = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelev']
    if a in list1:
        b = list1.index(a)
        print(list2[b])
    else:
        print("Error")

c = int(input())
num(c)

#       string to integer                
def num(a):
    list1 = [1,2,3,4,5,6,7,8,9,10,11,12]
    list2 = ['one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelev']
    if a in list2:
        b = list2.index(a)
        print(list1[b])
    else:
        print("Error")

c = input()
num(c)

