t1 = (1, 2, 3, 4, 0)
t2 = (3, 2, 5, 1, 0)
t3 = (4, 9, 3, 6, 7)
L = []

length1 = len(t1)
length2 = len(t2)
length3 = len(t3)
print(length1, length2, length3)

max_len = max(length1, length2, length3)
print(max_len)

i = 0
sum = 0
print(t1[1])
while(max_len):
    sum += t1[i] + t2[i] + t3[i]
    L.append(sum)
    i += 1
print(tuple(L))



