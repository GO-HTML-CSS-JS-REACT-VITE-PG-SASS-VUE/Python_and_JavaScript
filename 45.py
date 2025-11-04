k = 0
for i in range(100, 1000):
    nums = list(map(int, str(i)))
    a = 0
    for b in nums:
        a += b**len(nums)
    if a == i:
        print(a)
        k += 1
print("Количество чисел:", k)