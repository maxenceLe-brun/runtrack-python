#Job 11 :
L = [7, 11, 42, 39, 2]
def job11(L):
    for a in range(0,len(L)):
        L[a]+=1
    return L
L = job11(L)
print(L)
