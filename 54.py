from random import randint

a = []
for i in range(0,10):
    a.append(randint(-5, 5))
b = 0
for i in range(len(a)):
    if a[i] > 0:
        b += a[i]
print("Массив:", a)
print("Сумма положительных элементов:", b)