#Job 4 :
def crypt(words, n):
    alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    liste = list(words)
    result = ""
    for a in liste:
        for b in range(0,len(alphabet)):
            if a == alphabet[b]:
                result += alphabet[(b+n)%len(alphabet)]
        if a == " ":
            result += " "
    print(result)
