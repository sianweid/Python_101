# Sortieren von Datensätzen in Python

import random

data = [random.randint(0,100) for _ in range(20)]
print(data)


# sorted: neue Liste returned sorted()
# sort: in -place Sortierung .sort()

data.sort()
print(data)

data = [random.randint(0,100) for _ in range(20)]
print(data)

data_2 = sorted(data)
print(data_2)

# Sortierung Umkehren mit reverse

data.sort(reverse = True) # true für sortierung groß -> klein
print(data)

data.sort(reverse = False) # false standardm. gesetzt für aufsteigend
print(data)


# .sort gehört zu Klasse der Listen
# Sorted auf alles iterierbare anwendbar; auch strings ...

name = 'andreas'
name_sorted = sorted(name)
print(name_sorted)