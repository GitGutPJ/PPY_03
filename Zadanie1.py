napis1 = "Python 2023"
napis2 = "Python 2023"
napis3 = "Python 2023"

porownanie1 = bool(napis1 == napis2)
porownanie2 = bool(napis2 == napis3)

print(porownanie1)
print(porownanie2)

print("Typ napis1 = " + str(type(napis1)) + " typ napis2 = " + str(type(napis2)) + " typ napis3 = " + str(type(napis3)))
print('Adres napis1 = ' + str(hex(id(napis1))) + " adres napis2 = " + str(hex(id(napis2))) + " adres napis3 = " + str(hex(id(napis3))))