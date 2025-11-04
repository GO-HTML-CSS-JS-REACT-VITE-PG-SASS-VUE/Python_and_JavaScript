from random import randint

a = []
for i in range(0,10):
    a.append(randint(10, 100))
b = a.copy()
c = 0
for i in range(len(b) - 1):
    if (b[i] + b[i+1]) % 3 == 0:
        c += 1
print("Массив:", a)
print("Число пар элементов, сумма которых делится на 3:", c)