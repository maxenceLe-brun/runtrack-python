#Job 14 :
def my_long_word(n, word):
    allwords = [""]
    printing = ""
    for a in word:
        if a == " ":
            allwords += [" "]
        else:
            allwords[-1] += a
    for b in allwords:
        N = 0
        for c in b:
            N+=1
        if N > n+1:
            printing += b+" "
    return printing
