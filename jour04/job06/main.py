#Job 6 :
def job06(liste):
    if len(liste) == 0:
        print("you're kidding, right?")
    elif len(liste) == 1:
        print(liste)
    else:
        temp = liste[-1]
        liste[-1] = liste[0]
        liste[0] = temp
        print(liste)
job06()
