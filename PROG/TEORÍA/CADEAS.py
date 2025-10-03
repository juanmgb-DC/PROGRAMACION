c = "Esta é unha cadea de texto"
c1 = 'Onde podo escribir "secuencias" de caracteres'

for caracter in c:
    print(caracter)


print(c1[3])
print(c1[19:31])
print(c.count('a', 2,10))
print(c.count('a'))
print(len(c))
print(c.find('a'))
print(c.find('a',5,9))
print(c.join('123456789'))
print(c.partition(' '))
print(c.split(" "))