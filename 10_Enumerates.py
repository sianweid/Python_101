# Enumerates, einfaches Indexieren und Iterieren von Daten

smaller = [1,2,3]
names = ['jan', 'peer', 'gerd']

for i in range(len(names)):
    print(i, names[i])

# Besser:

for index, val in enumerate(names):
    print(index, val)


# Kombinierbar mit zip-Funktion

for number, (index_names, val) in zip(smaller, enumerate(names)):
    print(number, index_names, val)

    # Enumerate gibt Tupel () zurück

