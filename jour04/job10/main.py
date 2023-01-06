#Job 10 :
def job10():
    L = [8, 24, 27, 48, 2,16, 9, 102, 7, 84, 91]
    result = 1
    for a in L:
        if a >= 25 and a <= 90:
            result *= a
    print(result)
job10()
