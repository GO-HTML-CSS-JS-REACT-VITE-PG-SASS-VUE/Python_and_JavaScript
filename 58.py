from random import randint

a = []
for i in range(0,10):
    a.append(randint(0, 200))
b = a.copy()
c = 0
for i in range(len(b)):
    if len(str(b[i])) == 2:
        c += 1
print("Массив:", a)
print("Число двузначных чисел:", c)