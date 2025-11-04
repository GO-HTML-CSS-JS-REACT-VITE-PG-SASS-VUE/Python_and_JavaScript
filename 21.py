a = int(input("Введите возраст: "))
if a % 10 == 1:
    print("Вам", a, "год")
elif a % 10 == 2 or a % 10 == 3:
    print("Вам", a, "года")
else:
    print("Вам", a, "лет")