pierwsza = input('Podaj pierwsza liczbe')
druga = input('Podaj druga liczbe')
symbol = input('Podaj symobol operacji (+,-,*,/)')
pierwsza = int(pierwsza)
druga = int(druga)

def mathemax(znak):
    result = {
        '+': pierwsza + druga,
        '-': pierwsza - druga,
        '*': pierwsza * druga,
        '/': pierwsza / druga
    }
    return result.get(znak, "Zly znak")


print("Wynik: ",mathemax(symbol))

