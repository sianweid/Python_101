# Module laden und eigene erstellen
# Mathlib vorher installieren! => pip3 install matplotlib


import numpy as np   # Module müssen als Paket importiert werden; np konvention als abkürzung für numpy
import Eigenes_Modul



print(np.mean([1,2])) # Mittelwert aus numpy Modul


# from numpy import * # ges. numpy Paket wird importiert

from numpy import mean, median # gezielte Pakete können importiert werden aus numpy, s.d. "np." entfallen kann!

# Eigene Module importieren

val, a, b = Eigenes_Modul.func()
print(val)


