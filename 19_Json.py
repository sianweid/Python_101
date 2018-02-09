# JSON = JavaScript Object Notation
# Schnelles und einfaches Verwalten von Datensätzen

import json         # Json Modul importieren

personen = ['jan','peter','horst']
präferenzen = {'jan' : ['AI','ITS','Mathematik'],
            'peter' : ['ITS','ET','Physik'],
            'horst' : ['Physik','Mathematik','Chemie']}
noten = {'jan' : ['1','1','2'],
        'peter' : ['3','2','2'],
        'horst' : ['3','2','1']}

dict_student_2 = { pers : [( fach , note ) for fach, note in 
                        zip( präferenzen[ pers ] , noten[ pers ] ) ] 
                        for pers in personen}

with open('stud_noten.txt', 'w') as f:
    json.dump(dict_student_2, f, indent = 4, separators=(',',':'), sort_keys=True)
                            #   Einrücken      Trennen              Sortierung

# Pandas als Format, wenn mit excel arbeiten
