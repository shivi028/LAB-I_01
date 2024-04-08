string = 'i love python'
s1 = []
count = 0
key = set(string)
for i in key:
    for j in string:
        if i == j:
            count += 1
            s1.append(count)

print(s1)


