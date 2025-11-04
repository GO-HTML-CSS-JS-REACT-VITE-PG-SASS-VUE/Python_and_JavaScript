a = []
while True:
    a.append(int(input("Введите число (0 для завершения): ")))
    if a[-1] == 0:
        break
b = 0
for i in a:
    if i != 0 and i % 3 == 0:
        b += 1
print("Кол-во чисел, которые делятся на 3:", b)