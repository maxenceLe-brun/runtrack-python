#Job 3 :
def tapis(n):
    result = "+"+"-"*(n+1)+"+\n"
    for a in range(0,n+1):
        result += "|"
        result += "#"*(n-a)
        result += " "
        result += "#"*a
        result += "|\n"
    result += "+"+"-"*(n+1)+"+"
    print(result)
