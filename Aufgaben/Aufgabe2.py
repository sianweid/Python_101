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

dict_student = {}

for pers in personen:

        fach = präferenzen[pers]
        note = noten[pers]
        leistung = list(zip(fach,note))

        dict_student[pers] = leistung

print(dict_student)
        
for person, notenspiegel in dict_student.items():
        print('Name:   ', person)
        for fach in notenspiegel:
                print('Fach: ', fach[0], '   Note: ', fach[1])



# Version mit Comprehension

dict_student_2 = { pers : [( fach , note ) for fach, note in 
                        zip( präferenzen[ pers ] , noten[ pers ] ) ] 
                        for pers in personen}
# print(dict_student_2)

for person, notenspiegel in dict_student_2.items():
        print('Name:   ', person)
        for fach in notenspiegel:
                print('Fach: ', fach[0], '   Note: ', fach[1])

# Zusatzaufgabe

same_interest = { }

for person, fach in dict_student_2.items():
        for interesse in fach:
                if interesse[0] in same_interest.keys():
                        same_interest[interesse[0]].append(person)
                else:
                        same_interest[interesse[0]] = [person]  
print(same_interest)


