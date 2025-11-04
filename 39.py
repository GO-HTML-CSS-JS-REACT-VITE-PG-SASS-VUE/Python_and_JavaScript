import math

a = int(input("Введите натуральное число: "))
b = False
if (a >= 0):
    b = True
    for i in range(2, int(math.sqrt(a) + 1)):
        if a % i == 0:
            b = False
            break
if b:
    print("Число является простым.")
else:
    print("Число не является простым.")