print("Введите три числа:")
a = int(input())
b = int(input())
c = int(input())
ans1 = a + b + c
ans2 = a * b * c
ans3 = ans1 / 3
print(a, "+", b, "+", c, "=", ans1, sep="")
print(a, "*", b, "*", c, "=", ans2, sep="")
print("(", a, "+", b, "+", c, ")/3", "=", ans3, sep="")