#For Schleife

# i als Zählvariable
# i im Bereich [0,...,9] da range von 0 los zählt
# wenn i als zählvariable nicht benötigt kann man auch Platzhalter _ verwenden

for i in range(10):
    print(i)
    
    zahl = int(input('Geben Sie eine Zahl ein:\n'))

    if zahl < 10:
        print('Die Zahl ist kleiner als 10') #TAB wichtig für validen Code, aber keine {...} in if-case

    elif zahl >= 10 and zahl < 20:
        print('Die Zahl ist mindestens 10, aber kleiner als 20')

    else:
        print('Die Zahl ist größer als 20')

    weiter = int(input('Weiterspielen? (0 für nein; 1 für ja)\n'))

print('Ende :)')

einkaufsliste = ['apfel','birne','gemüse']
for item in einkaufsliste:
    print(item)

# for-Schleifen verwendbar mit ranges, Listen ... 
