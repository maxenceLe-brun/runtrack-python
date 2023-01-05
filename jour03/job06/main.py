#Job 6 :
def pyramide():
    origin = "abcdefghijklmnopqrstuvwxyz" * 10
    used = ""
    backward = ""
    using = "a" 
    n = 1
    while used < origin and len(using) > len(backward):
        print(using)
        backward = using
        used += using
        n += 1
        using = origin[len(used):len(used)+n]
