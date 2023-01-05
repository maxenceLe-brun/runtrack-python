#Job 4 :
def nombres_transforme():
    for a in range(1,101):
        b = ""
        if a%3 == 0: b += "Fizz"
        if a%5 == 0: b += "Buzz"
        if b == "": b = a
        print(b)
