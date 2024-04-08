dic1 = {1:10, 2:20}
dic2 = {3:30, 4:40}
dic3 = {5:50, 6:60}
def Merge3(d1, d2, d3):
    return d1 | d2 | d3

print(Merge3(dic1, dic2, dic3))