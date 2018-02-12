# Basics für Numpy Listen und Funktionen

import numpy as np

data = [1.0, 2.0, 3.0]
print(data)

# numpy Arrays

data2 = np.asarray(data, dtype = np.float)
print(data2)

data3 = np.array([1.0, 2.0, 3.0], dtype = np.float)

# Wenn Inhalt der Liste noch nicht bekannt ==> Initialisierung

data4 = np.zeros(shape=(10), dtype=np.float)
print(data4)

data4 = np.full(4, 255)
print(data4)

matrix = np.zeros(shape=(3,3), dtype = np.int8)
print(matrix)

listeMatrix = matrix.reshape(9)
print(listeMatrix)