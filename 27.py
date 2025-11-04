a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))
M = 0
if a > b:
    M = a
elif c > b:
    M = c
else:
    M = b
print(M)