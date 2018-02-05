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

# Iterieren von Listen

for i in range(len(einkaufsliste)): 
    print(einkaufsliste[i])

# besser
for val in einkaufsliste:
    print(val)
