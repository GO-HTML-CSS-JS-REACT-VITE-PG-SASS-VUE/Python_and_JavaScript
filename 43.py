k = 0
for i in range(1, 1000):
    if i % 15 == 11 and i % 11 == 9:
        print(i)
        k += 1
print("Количество чисел:", k)