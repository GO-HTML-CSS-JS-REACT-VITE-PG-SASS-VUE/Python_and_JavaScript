a, b = map(int,input("Введите два числа: ").split())
c = 0
for i in range(b):
    c += a
print(a, "*", b, "=", c)