#Job 9 :
def job09():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    minmax = [max(L),min(L)]
    for a in L:
        if a < minmax[0]:
            minmax[0] = a
        if a > minmax[1]:
            minmax[1] = a
    if minmax[0] == min(L) and minmax[1] == max(L):
        print(minmax[0],minmax[1])
    else:print("ratio")
job09()
