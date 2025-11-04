from random import randint

p1 = randint(1,9)
p2 = randint(0,9)
p3 = randint(0,9)
nums = [str(p1), str(p2), str(p3)]
print("Получено число:", "".join(nums))
print("Сотни:", p1)
print("Десятки:", p2)
print("Единицы:", p3)