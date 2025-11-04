a = int(input("Введите число: "))
b = 0
while a != 0:
    if (a // 10 % 10 == a % 10):
        b += 1
    a = a // 10
if b:
    print("да.")
else:
    print("нет.")