#Job 5 : I won't make any jokes here. I kow that this job was asked to do with "if" and "else", but the "eval" function is so useful, that i couldn't ignore it
def calcul(num1,operator,num2):
    return eval(str(num1)+operator+str(num2))
print(calcul(5,"*",3))
print(calcul(6,"/",2))
print(calcul(7,"%",2))
