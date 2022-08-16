# Avoiding duplactes

n = input()
s = []
s.append(n)

while n!=" ":
    n = input()
    if n!=" ":
        if n not in s:
            s.append(n)

print(s)

