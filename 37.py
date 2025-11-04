a = []
while True:
    a.append(int(input("Введите число (0 для завершения): ")))
    if a[-1] == 0:
        break
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)
print("Максимальное число из четных:", max(b))