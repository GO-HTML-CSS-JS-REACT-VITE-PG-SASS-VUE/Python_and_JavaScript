print("Введите номер урока:")
a = int(input())
les = (a * (45 + 10) + 500)
les_hour = les // 60
les_min = les % 60
print(f"{les_hour:02d}", f"{les_min:02d}", sep="-")