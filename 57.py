from random import randint

a = []
for i in range(0,10):
    a.append(randint(0, 200))
b = a.copy()
c = 0
for i in range(len(b)):
    if b[i] % 10 == 0:
        c += 1
print("Массив:", a)
print("Число элементов, которые делятся на 10:", c)