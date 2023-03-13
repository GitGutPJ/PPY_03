pierwsza = input('Podaj pierwsza liczbe')
symbol = input('Podaj symobol operacji (+,-,*,/)')
druga = input('Podaj druga liczbe')
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


print(mathemax(symbol))
