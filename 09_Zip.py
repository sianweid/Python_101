# ZIP, Praktisches Zusammenführen von Daten


# Gleichzeitiges Ausgeben von Werten aus 2 Listen
# Hört bei kleinerer Liste auf, wenn unterschiedlich lang!

smaller = [1,2,4,6]
name =['jan', 'peter', 'horst', 'python']

for val1, val2 in zip(smaller, name):
    print(val1, val2)


neue_liste = list(zip(smaller, name))   # ZIP Objekt muss zur Liste gecastet werden, um diese mittels print ausgeben zu können 
print(neue_liste)

for val in neue_liste:
    print(val[0], val[1])
    print(val)

# () = Tupel
# [] = Liste
# {} = Dictionary
