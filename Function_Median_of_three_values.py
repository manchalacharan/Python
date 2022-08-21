#Let us creat a function
def median(a,b,c):
    mn = min(a,b,c)
    mx = max(a,b,c)
    md = (a+b+c)-(mn+mx)
    print(md)

x = int(input())
y = int(input())
z = int(input())
median(x,y,z)
