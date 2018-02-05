# Aufgabe 1
# Lege eine Liste "data" mit zufälligen Werten an
# Lese dann per Nutzereingabe eine Integer Variable ein
# Iteriere dann über alle Werte der data Liste
# Entscheide beim Iterieren der Liste "data", ob der aktuelle Wert
# kleiner als die Nutzereingabe ist => Wert kommt in die smaller Liste
# oder größer ist => Wert kommt in die bigger Liste

# Zusatz: Zufallsliste mit List Comp anlegen

import random

UB = 100
LB = 0

random_list = [random.randint(LB,UB) for _ in range(10)]
print(random_list)

smaller = []
bigger = []

user_input = int(input("Geben Sie eine Zahl im Bereich 0 bis 100 ein!\n"))

for val in random_list:

    if val < user_input:
        smaller.append(val)

    elif val > user_input:
        bigger.append(val)

print(smaller)
print(bigger)