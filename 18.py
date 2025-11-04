a = input("Возраст Антона: ")
b = input("Возраст Бориса: ")
c = input("Возраст Виктора: ")
if a > b and a > c and b != c:
    print("Антон старше всех.")
elif b > a and b > c and a != c:
    print("Борис старше всех.")
elif c > a and c > b and a != b:
    print("Виктор старше всех.")
elif a == b and a > c:
    print("Антон и Борис старше Виктора.")
elif a == c and a > b:
    print("Антон и Виктор старше Бориса.")
elif c == b and c > a:
    print("Борис и Виктор старше Антона.")
elif a == b and a < c:
    print("Виктор старше Антона и Бориса.")
elif a == c and a < b:
    print("Борис старше Антона и Виктора.")
elif c == b and c < a:
    print("Антон старше Бориса и Виктора.")
else:
    print("Все одного возраста.")