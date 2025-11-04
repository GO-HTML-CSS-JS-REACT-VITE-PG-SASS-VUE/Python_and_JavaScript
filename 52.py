from random import randint

a = []
for i in range(0,10):
    a.append(randint(100, 300))
b = a.copy()
for i in range(len(b)):
    b[i] = b[i] // 10 % 10
print("Массив:", a)
print("Число десятков:", b)