l1 = [(10, 20, 30), (40, 50, 60), (70, 80, 90)]

for i in range(len(l1)):
    l2 = list(l1[i])
    l2[-1] = 100
    l1[i] = tuple(l2)

print(l1)