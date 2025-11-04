a = int(input("Введите натуральное число: "))
c = a
b = []
for i in range(0,5):
    a -= 1
    b.append(a)
b = list(reversed(b))
b.append(c)
for i in range(0,5):
    c -= 1
    b.append(c)
print(b)