# Aufgabe 2

# Anlegen eines Dictionarys, was für mehrere Personen
# welches für meherere Personen die jeweiligen Vertiefungsgebiete
# und Noten in einem gemeinsamen Dictionary abspeichert Danach wird dann
# über das Dict iteriert und die einzelnen Werte jeder Person ausgegeben
#
# Zusatzaufgabe:
# Gebe die Personen aus, die die gleichen Interessen haben!

personen = ['jan','peter','horst']
präferenzen = {'jan' : ['AI','ITS','Mathematik'],
            'peter' : ['ITS','ET','Physik'],
            'horst' : ['Physik','Mathematik','Chemie']}
noten = {'jan' : ['1','1','2'],
        'peter' : ['3','2','2'],
        'horst' : ['3','2','1']}

stud_dict = {key: (val1,val2) for key, (val1,val2) in zip(präferenzen, noten)}
print(stud_dict)