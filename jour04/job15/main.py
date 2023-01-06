#Job 15 :
def job15():
    liste = [22.4, 4.0, 16.22, 9.10, 11.00, 12.22, 14.20, 5.20, 17.50]
    L = []
    for a in liste:
        L += [a//1]
        if a%1 >= 0.5:
            L[-1] += 1
    return L
