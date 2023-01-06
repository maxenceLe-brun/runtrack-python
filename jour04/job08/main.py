#Job 8 :
def job08():
    L = [8, 24, 27, 48, 2,16, 9, 7, 84, 91]
    result = 0
    for a in L:
        if a%2 == 0:
            result += a
    print(result)
job08()
