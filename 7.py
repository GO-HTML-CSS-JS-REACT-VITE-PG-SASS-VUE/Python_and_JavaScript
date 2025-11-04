print("Введите число секунд:")
a = int(input())
ans_hour = a // 60 // 60
ans_min = a // 60 % 60
ans_sec = a % 60 % 60
print(ans_hour, "ч.", ans_min, "мин.", ans_sec, "с.")