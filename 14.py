from random import randint

print("Выпало очков:")
p1 = randint(1,9)
print(p1)
p2 = randint(1,9)
print(p2)
p3 = randint(1,9)
print(p3)
a = int(str(p1) + str(p2) + str(p3))
b = a**2
print("Число:", a)
print("Его квадрат:", b)