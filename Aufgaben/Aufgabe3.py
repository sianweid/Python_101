# Aufgabe 3
#
# Schreibe eine Funktion, die die Zahl PI annäert
#
# Formel: 
# x_i = (i - (1/2)) / n
# f(x_i) = 4 / (1 +x_i^2)
# PI = 1/n * Sum_1^n f(x_i)
# Syntax Sum_1^n bedeutet: "Starte bei i=1 und gehe bis n und bilde Summe"
#
# Zusatzaufgabe: Vergleiche das Ergebnis mit numpy's PI
# Wie viele Nachkommastellen stimmen mit n=100, 1000, 10000
# überein?

import numpy as np
pi = np.pi


def xi(i,n):
    x = ( i - (1.0/2.0)) / n
    return x


def fi(x_i):
    f = 4.0 / (1.0 + x_i ** 2.0)
    return f

def calc_pi():
    n = 100000
    pi = 0.0
    
    for i in range(1,n):
        pi += fi(xi(i,n))
    pi /= n

    print('Eigenes PI: ', pi)
    print('Numpy PI: ',np.pi)
    print('Differenz: ', pi-np.pi)

calc_pi()

