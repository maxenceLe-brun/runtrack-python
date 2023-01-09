#Job 2 :
def rectangle(width,height):
    result = ""
    for a in range(0,height):
        for b in range(0, width):
            if 0<b<width-1 and 0<a<height-1:
                result += " "
            if b == width-1:
                result += "|\n"
            if b == 0:
                result += "|"
            if 0<b<width-1 and (a == 0 or a == height-1):
                result += "-"
    print(result)
