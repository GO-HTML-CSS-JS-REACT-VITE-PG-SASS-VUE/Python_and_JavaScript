a = int(input("Введите номер месяца: "))
if a >= 3 and a <= 5:
    print("Весна.")
elif a >= 6 and a<= 8:
    print("Лето.")
elif a >= 9 and a<= 11:
    print("Осень.")
elif a == 12 or a == 1 or a == 2:
    print("Зима.")
else:
    print("Неверный номер месяца.")