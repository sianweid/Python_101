# Daten lesen und schreiben

text = 'fuu'
text2 = 'baa'
data = [1,3,5,7,9,11]

# w = (über-)schreiben, r = lesen, a = append , auch mischmodi möglich!


# Daten schreiben
with open('testfile', 'w') as f: # f als Konvention für name des fileOjekts!
    f.write(text + '\n')         # text muss string sein, dass \n Zeilenumbruch ausführbar. \n nur mit string konkatenierbar
    f.write(text2)


# Daten lesen

# readline() ... liest string ein. wenn mit ggf zahlen rechnen => cast zu float oder int!

text_neu = ''

with open('testfile','r') as f:
    # print(f.readline()) #... Zeile 1              Zeile für Zeile => mehrere readline() Kommandos hintereinander
    # print(f.readline()) #... Zeile 2

    print(f.read()) # Gibt ges. eingelesenes Dokument zurück 


    # f.readlines() # Alles
    # print(list(f)) # gibt liste zurück
    
    for line in f:
         print(line)

    for line in f:
        text_neu += line
    print(text_neu)

    # text_neu = f.readlines() # Rückgabe als Liste! 
    # print(text_neu)


with open('data.txt','a') as f:
    for val in data:             # data - Liste iterieren, ! Liste => string-Cast nötig
        f.write(str(val) + ', ') # write nur mit string
