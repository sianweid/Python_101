# Module importieren

import statistics   # Statistik Paket nun verwendbar statistics.variance()

import statistics as s  # optional s.variance()

from statistics import variance # variance()

from statistics import variance, mean # meherere fkt importieren

# from statistics import * # alle fkt aus dem Paket sind importiert und können ohne Paketverweis aufgerufen werden



# Module erstellen
# Modul prinzipiell nichts anderes als normales Skript
# Liegt im gleichen Ordner wie Stammdaten


def ex(var):
    print(var)
