string = input('enter a string\n')
# res = []
new_string = []
for i in string.lower():
    if(i == 'a'):
        new_string.append('x')
    elif(i == 'b'):
        new_string.append('y')
    elif(i == 'c'):
        new_string.append('z')
    res = (ord(i))
    new_string.append(chr(res - 3))

# print(type(str(new_string)))
print(str(new_string))