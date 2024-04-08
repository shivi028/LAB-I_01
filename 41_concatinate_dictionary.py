dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}

# METHOD 1  using update
def Merge(d1, d2):
    return(d1.update(d2))

# return none
Merge(dic1, dic2)
Merge(dic1, dic3)

# print actual changes
print(dic1)

# METHOD 2  passing multiple arguments
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
def Merge2(d1, d2, d3):
    res = {**d1, **d2, **d3}
    return res
print(Merge2(dic1, dic2, dic3))


# METHOD 3   using expression
dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
def Merge3(d1, d2, d3):
    return d1 | d2 | d3

print(Merge3(dic1, dic2, dic3))
