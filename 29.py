a = int(input("Введите число: "))
b = len(str(a)) - len(str(a).replace("1",""))
print("Единиц:", b)