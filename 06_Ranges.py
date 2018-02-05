# Range Anweisungen

# range(start, stop, step)
# range(0, 3, 1) => 0, 1, 2
# entspricht der Eingabe range(3)

for i in range(10):
    print(i)

for i in range(10, 21, 2):
    print(i)




for i in range(2):
    print(i)
    
    zahl = int(input('Geben Sie eine Zahl ein:\n'))

    if zahl < 10:
        print('Die Zahl ist kleiner als 10') #TAB wichtig für validen Code, aber keine {...} in if-case

    elif zahl >= 10 and zahl < 20:
        print('Die Zahl ist mindestens 10, aber kleiner als 20')

    else:
        print('Die Zahl ist größer als 20')