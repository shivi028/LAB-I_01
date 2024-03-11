a = int(input('enter the value\n'))
j = 0
for i in range(1, a+1):
    for space in range(1, (a-i)+1):
        print(end=' ')

    while j!=(2*i-1):
        print('* ', end='')
        j += 1
    
    j = 0
    print()