#Job 12 :
L = []
for a in liste:
    L += [a]
result = []
while L != []:
    MIN = L[0]
    for a in L:
        if a < MIN:
            MIN = a
        else:
            print(a)
    l = []
    for b in L:
        if MIN == b:
            result += [MIN]
        else:
            l += [b]
    L = l
#print(result)
