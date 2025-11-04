from random import randint

a = []
for i in range(0,10):
    a.append(randint(-2, 2))
b = 1
for i in range(len(a)):
    if a[i] != 0:
        b *= a[i]
print("Массив:", a)
print("Произведение ненулевых элементов:", b)