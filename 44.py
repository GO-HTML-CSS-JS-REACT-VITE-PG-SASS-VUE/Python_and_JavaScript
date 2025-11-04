a = int(input("Введите натуральное число: "))
b = 1
for i in range(1, a + 1):
    b *= i
print("Факториал равен:", b)