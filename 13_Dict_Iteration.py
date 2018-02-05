# Dict Iteration, Wie auf Keys und Values zugreifen?

tagebuch = {'montag':'doofer tag', 'dienstag':'besserer tag'}

tagebuch2 = {'montag':['wochenbeginn', 'planung woche'],
            'dienstag':['wochenmitte','planungsabschluss']}

tagebuch3 = {'montag':{'morgens':'brot','mittags':'spaghetti','abends':'brot'},
            'dienstag':{'morgens':'müsli','mittags':'pizza','abends':'auflauf'}}


# Schlechte Variante, da mit Liste verwechselbar
for val in tagebuch3:
    print(val)

# Besser, da Dict erkennbar
for k in tagebuch3.keys():
    print(k)


# Rückgabe von Keys und Values
for k, v in tagebuch3.items():
    print(k,'     ',v)

# Vgl mit Enumerate
for k, v in enumerate(tagebuch3):
    print(k, '            ',v)

# Wenn nur Value benötigt wird
for  val in tagebuch.values():
    print(val)

for k, liste in tagebuch2.items():
    for val in liste:
        print(val)