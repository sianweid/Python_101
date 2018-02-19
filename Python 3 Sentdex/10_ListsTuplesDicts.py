# Tuple kann nicht geändert werden
# Listen dürfen modifiziert werden

# Tupel:
x = 2,4,5,2,4
b = (3,5,2,6,2,2)

# Liste
y = [3,5,2,1,8,1]


# Bsp Tupel

def exfunc():
    return 15,7

o,u = exfunc()          # Hier ist ein Tupel praktisch, da die Reihenfolge von x und y bei Ausgabe nicht verändert werden kann
                        # Auch gut bei eingelesenen Daten aus Dateien


print(x[1])             # Ausgabe der Nummer am Index 1
print(y[1])



# Listen manipulieren

z = [1,4,5,6,2,55,2,3,678,34]

z.append(2)     # Modifiziert z und fügt 2 hinzu
z.insert(4,2)   # Fügt an Index 4 eine 2 hinzu
z.remove(2)     # Entfernt die erste 2 der Liste
z.remove(x[3])  # Entfernt den Index 3
z.count(6)      # Zählt wie viele "6" in der Liste
z.sort()        # Sortiert die EInträge der Liste







