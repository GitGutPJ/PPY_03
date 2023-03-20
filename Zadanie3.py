zapytanie = 'pytanie:'
odpowiedz = 'odpowiedz:'


pytanie1 = input(f'{zapytanie} Jak masz na imie i nazwisko?')
pytanie1=pytanie1.title()
print(f'{odpowiedz} {pytanie1}')

pytanie2 = input(f'{zapytanie}  Najczestszym sposobem spędzania wolnego czasu jest dla Ciebie:\na) sluchanie muzyki\nb) podrozowanie\nc) uprawianie sportu')
if pytanie2=='a' :
 print(f'{odpowiedz} sluchanie muzyki')
elif pytanie2=='b' :
 print(f'{odpowiedz} podrozowanie')
elif pytanie2 == 'c':
 print(f'{odpowiedz} uprawianie sportu')
else :
 print(f'{odpowiedz} inne')

pytanie3 = input(f'{zapytanie}  W jakich okolicznosciach czytasz ksiazki najczesciej?\na) podczas podrozy\nb) w czasie wolnym(po pracy, na urlopie)\nc) podczas pracy/nauki')
if pytanie3=='a' :
 print(f'{odpowiedz} podczas podrozy')
elif pytanie3=='b' :
 print(f'{odpowiedz} w czasie wolnym(po pracy, na urlopie)')
elif pytanie3 == 'c':
 print(f'{odpowiedz}  podczas pracy/nauki')
else :
 print(f'{odpowiedz} inne')


pytanie4 = input(f'{zapytanie}  Jezeli spęezasz czas wolny czytajac ksiazki, jaki jest glowny powod takiego wyboru?\na) chec poszerzenia wiedzy\nb) czytanie mnie relaksuje/odpreza\nc) czytanie to moje hobby')
if pytanie4=='a' :
 print(f'{odpowiedz} chec poszerzenia wiedzy')
elif pytanie4=='b' :
 print(f'{odpowiedz} czytanie mnie relaksuje/odpreza')
elif pytanie4 == 'c':
 print(f'{odpowiedz} czytanie to moje hobby')
else :
 print(f'{odpowiedz} inne')

