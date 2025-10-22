t= (6,7,10,9,10)

def esta_ordeada(t):
    i = 0
    while i < len(t) - 1:
        if t[i] > t[i + 1]:
            return False
        i = i + 1
    return True
print(esta_ordeada(t))