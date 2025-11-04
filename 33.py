from tabulate import tabulate

a = [64168, 358853, 6365133, 17905514, 549868978]
b = [82678, 691042, 11494962, 23108855, 298294835]
c = a.copy()
d = b.copy()
e = []
i = 0

while i != len(c) :
    while c[i] != 0 and d[i] != 0:
        if c[i] > d[i]:
            c[i] = c[i] % d[i]
        else:
            d[i] = d[i] % c[i]
    e.append(c[i] + d[i])
    i += 1

ans = [["a"], ["b"], ["НОД(a,b)"]]
for j in a:
    ans[0].append(j)

for j in b:
    ans[1].append(j)

for j in e:
    ans[2].append(j)

print(tabulate(ans, tablefmt='fancy_grid'))