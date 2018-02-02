#While Schleifen

zahl = 0.0
ergebnis = 25
weiter = True

while weiter:
    zahl = int(input('Geben Sie eine Zahl ein:\n'))

    if zahl < 10:
        print('Die Zahl ist kleiner als 10') #TAB wichtig für validen Code, aber keine {...} in if-case

    elif zahl >= 10 and zahl < 20:
        print('Die Zahl ist mindestens 10, aber kleiner als 20')

    else:
        print('Die Zahl ist größer als 20')

    weiter = int(input('Weiterspielen? (0 für nein; 1 für ja)\n'))

print('Ende :)')