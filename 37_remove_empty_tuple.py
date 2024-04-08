l1 =  [(10, 20, 30), (), (40, 50, 60), (70, 80, 90), ()]
count = 0

# for i in range(len(l1)):
#     l2 = list(l1[i])
#     print(l2)


for i in range(len(l1)):
    l2 = list(l1[i])
    count = 0
    for j in range(len(l2)):
        count += 1
    if(count == 0):
        del l1[i]
    else:
        l1[i] = tuple(l2)
    
    print(l1)

