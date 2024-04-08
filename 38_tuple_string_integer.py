t1 = (('111', '11'), ('222', '22'), ('333', '33'))
index = 0
L = list(t1)


for i in range(len(t1)):
    t2 = list(t1[i])
    j = 0
    for i in t2:
       t2[j] = int(i)
       j += 1
    L[index] = tuple(t2)
    index += 1

print(tuple(L))
        