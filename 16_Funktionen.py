# Funktionen erstellen


def func(a=None, b=None, c=None):  # None falls keine Parameter übergeben werden => keine Argumente bei Funktionsaufruf nötig

    print('A: ',a)
    print('B: ',b)
    print('C: ',c)

    val = a * b

    return val, a, b


# Ausgabe aus Funktion

wert, a , b = func(1,2)

print(wert, a , b)
