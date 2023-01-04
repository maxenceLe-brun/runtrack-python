#... pour aller plus loin. Oh my god, i'm speedrunning a migraine
from math import*
def test(a,b,c):
    if c > a+b or b > a+c or a > b+c:
        print("triangle impossible")
    elif (a == b == c):
        print("Bien joué, c'est un triangle equilateral!")
    elif (a == b and sqrt(a**2 + b**2) == c) or (b == c and sqrt(b**2 + b**c) == a) or (c == a and sqrt(c**2 + a**2) == b):
        print("c'est un triangle rectangle isocèle!")
    elif (a == b and sqrt(a**2 + b**2) != c) or (b == c and sqrt(b**2 + b**c) != a) or (c == a and sqrt(c**2 + a**2) != b):
        print("c'est un triangle isocele")
    elif (a != b and sqrt(a**2 + b**2) == c) or (b != c and sqrt(b**2 + b**c) == a) or (c != a and sqrt(c**2 + a**2) == b):
        print("c'est un triangle rectangle")
    elif (a != b and sqrt(a**2 + b**2) != c) or (b != c and sqrt(b**2 + b**c) != a) or (c != a and sqrt(c**2 + a**2) != b):
        print("c'est un triangle lambda")
    else:
        print("ratio")
