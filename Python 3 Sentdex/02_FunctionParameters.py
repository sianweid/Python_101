def simple_addition(num1, num2):
    answer = num1 + num2
    print('Berechnung...')
    print('Antwort:', answer)

simple_addition(5,3)

# Zahl der Variablen in Funktion ist nicht festgelegt, keine Einschränkung
# Die Reihenfolge der übergebenen Zahlen ist jedoch wichtig!

# Spezifizierung der übergebenen Variablen kann hier ggf. absichern!
# Andere Reihenfolge, aber die Variablen werden noch mal festgelegt, s.d. eine 
# eindeutige Zuordnung möglich ist

simple_addition(num2=2, num1= 34)

# Übergabe von default-Parametern in Funktionen möglich

def sim_fkt(num1, num2):
    pass

def simple(num1, num2 = 5):
    print(num1, num2)

simple(2,2)