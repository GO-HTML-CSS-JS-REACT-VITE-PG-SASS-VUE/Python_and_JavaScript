a = []
while True:
    a.append(int(input("Введите число (0 для завершения): ")))
    if a[-1] == 0:
        break
b = 0
for i in a:
    if len(str(i)) == 2:
        if i % 10 == 3:
            b += 1
print("Кол-во двузначных чисел, которые заканчиваются на 3:", b)