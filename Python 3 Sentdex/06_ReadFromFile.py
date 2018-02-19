# Aus Datei einlesen

readMe = open('exampleFile.txt', 'r').read() # ges. Dokument wird gelesen
print(readMe)


# Optional

readMe = open('exampleFile.txt', 'r').readlines() # speichert eingelesene Daten als python-Liste readMe
print(readMe)

