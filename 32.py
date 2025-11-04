a, b = map(int, (input("Введите два числа: ")).split())
c = a
d = b
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
print("НОД(", c, "," , d, ")=", a + b, sep="")