#Job 5 :
from random import*
def job05():
    long = randrange(5,15000)
    L = []
    for a in range(long):
        L.append(randrange(1,340))
    print(L[1])
    L[3] = L[2] + L[4]
    print(L[-1])
    print(L)
job05()
