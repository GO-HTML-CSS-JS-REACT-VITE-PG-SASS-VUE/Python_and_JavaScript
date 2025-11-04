k = 0
for i in range(1000, 10000):
    if i % 7 == 0:
        print(i)
        k += 1
print("Количество чисел:", k)