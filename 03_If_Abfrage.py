#If, Elif, Else Abfragen

zahl = 0.0
zahl = int(input("Geben Sie eine Zahl ein:\n")) #Eingabe der Zahl durch den Benutzer als Integer; \n für neue Zeile

if zahl < 10:
    print('Die Zahl ist kleiner als 10') #TAB wichtig für validen Code, aber keine {...} in if-case

elif zahl >= 10 and zahl < 20:
    print('Die Zahl ist mindestens 10, aber kleiner als 20')

else:
    print('Die Zahl ist größer als 20')
