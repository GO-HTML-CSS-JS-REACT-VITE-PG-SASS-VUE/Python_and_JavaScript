from random import randint

a = []
for i in range(0,10):
    a.append(randint(100, 500))
b = a.copy()
for i in range(len(b)):
    nums = list(map(int, str(b[i])))
    d = 0
    for c in nums:
        d += c
    b[i] = d
print("Массив:", a)
print("Сумма цифр:", b)