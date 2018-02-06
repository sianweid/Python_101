# Listen in Python
# a = a + b oder a += b?
# extend oder append?
# insert, pop, count, iterieren?

# dynamisch, kein starres array!


einkaufsliste = ['milch','salz','eier','äpfel']
zusatzliste = ['öl','mehl']
zusatzliste_2 = 'brot'

# Listen zusammenfügen (konkatenieren)

# einkaufsliste = einkaufsliste + zusatzliste # niemals machen! kostet resourcen
# einkaufsliste += zusatzliste

einkaufsliste.extend(zusatzliste)
print(einkaufsliste)
einkaufsliste.append(zusatzliste_2)
print(einkaufsliste)


# pop: wenn keine eingabe in klammern wird letztes element gelöscht
einkaufsliste.pop()
print(einkaufsliste)

# count-Funktion
print(einkaufsliste.count('milch'))

# Iterieren von Listen (engl.: iterable)
# etwas Punkt für Punkt durchgehen
# iterables in python: string, Tupel, Liste, Dictionary

for i in range(len(einkaufsliste)): 
    print(einkaufsliste[i])

# besser => print für jeden Listeneintrag ausführen
for val in einkaufsliste:
    print(val)


# Tupel ()
# entspricht dem Wort Datensatz, Einträge nicht veränderbar
# Häufig in Datenbanken vorhanden, z.B. SQL

a = (4,1,5,5,7)
print(a[1])

print(a[len(a)-1]) # Ausgabe des letzten Eintrags; Vorsicht, da erster Eintrag Index "0"



# sONSTIGES

a[1:4] # alle Variablen zwischen Stelle 1 und 4; nützlich bei Strings! Gibt Subliste/-string... aus

b = '345.362254373'
print(b.find('.')) # Stelle des "." in string-gecasteter Zahl
print(b[b.find('.') + 1 : ]) # Ausgabe aller Nachkommastellen

#


