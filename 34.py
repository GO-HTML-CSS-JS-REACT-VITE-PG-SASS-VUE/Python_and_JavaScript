print("Введите два числа:")
a,b = map(int, input().split())

c = a
d = b

e = 0
f = 0

while a != b:
    if a > b:
        a -= b
    else:
        b -= a
    e += 1

while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
    f += 1

print("НОД(", c, "," , d, ")=", a + b, sep="")
print("Обычный алгоритм:", e)
print("Модифицированный:", f)