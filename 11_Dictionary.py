# Dictionarys in Python {key: Value}


tagebuch = {'montag': 'wochenbeginn', 'dienstag':'dienstreise'}
print(tagebuch)

tagebuch = {'montag': ['wochenbeginn','alles doof'], 'dienstag':'dienstreise'}
tagebuch = {'montag': ['wochenbeginn','alles doof'], 0:'dienstreise'}

# Dictionarys sortieren um, oder nach Keys suchen

tagebuch = {'montag': {'wochenbeginn':'8.00','mittags':'alles doof'}, 
            'dienstag':['dienstreise', 'kostenabrechnung']}

print(tagebuch['montag']['mittags'])


# Beispiel
# Hashtable => Zusammengehörende Variablen - hier Key:Item - werden deklariert

a = {'Hallo':'Hello', 'Willkommen':'Welcome'}
print(a)

a['Tschüss'] = 'ByeBye' # erzeugt neuen Eintrag im Dictionary a


