from random import randint

a = []
for i in range(0,10):
    a.append(randint(0, 10))
b = a.copy()
for i in range(len(b)):
    b[i] **= 2
print("Массив:", a)
print("Квадраты:", b)