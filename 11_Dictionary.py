# Dictionarys in Python {key: Value}


tagebuch = {'montag': 'wochenbeginn', 'dienstag':'dienstreise'}
print(tagebuch)

tagebuch = {'montag': ['wochenbeginn','alles doof'], 'dienstag':'dienstreise'}
tagebuch = {'montag': ['wochenbeginn','alles doof'], 0:'dienstreise'}

# Dictionarys sortieren um, oder nach Keys suchen

tagebuch = {'montag': {'wochenbeginn':'8.00','mittags':'alles doof'}, 
            'dienstag':['dienstreise', 'kostenabrechnung']}

print(tagebuch['montag']['mittags'])
