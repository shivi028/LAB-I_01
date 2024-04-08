l1 = ['shivi','siddhant','bottle','phone','laptop']
specific_loc = int(input('enter the no. from which you want to reverse the list'))

s = 0
# e = len(l1) - 1

# not considering the first value
e = specific_loc - 1

# also changing on input of 1
e = specific_loc 
while(s <= e):
    temp = l1[s]
    l1[s] = l1[e]
    l1[e] = temp
    s += 1
    e -= 1

print(l1)