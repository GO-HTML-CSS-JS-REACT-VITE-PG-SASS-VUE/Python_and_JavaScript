from random import randint

a = []
for i in range(0,20):
    a.append(randint(100, 1000))
print("Массив:", a)
print("Сумма элементов первой половины массива:", sum(a[:len(a)//2]))
print("Сумма элементов второй половины массива:", sum(a[len(a)//2:]))