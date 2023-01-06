#Job 13 :
def job13():
    new = [10,20,30,20,10,50,60,40,80,50,40]
    result = []
    n = 2
    while n > 1 and new != []:
        n = 2
        forward = []
        result += [new[0]]
        for a in new:
            if new[0] != a:
                forward += [a]
            else:
                n += 1
        new = forward
        if n == 2:
            n = 1
    return result
