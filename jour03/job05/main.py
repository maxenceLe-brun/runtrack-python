#Job 5 :
def nombres_premiers():
    for a in range(2,1000):
        n = 0
        for b in range(1,a+1):
            if int(a/b) == a/b:
                n += 1
        if n == 2:
            print(a)
