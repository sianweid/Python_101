# Vererbung in Python




class Tier:
    rasse = ''
    geschlecht = ''
    alter = 0

    def __init__(self, rasse, geschlecht, alter):
        self.rasse = rasse
        self.geschlecht = geschlecht
        self.alter = alter

    def printRasse(self):
        print('Rasse: ', self.rasse)

# Vererbung aus Hauptklasse
# Neue Unterklasse
# Properties der Hauptklasse müssen ebenfalls im Contructor enthalten sein!

class Hund(Tier):
    zahl_beine = 0

    def __init__(self, zahl_beine, rasse, geschlecht, alter):
        # Vererbung => Kontruktor aus Hauptklasse muss zunächst aufgerufen werden // Superconstructor; bei P3 nicht nötig, aber in super kann Elternklasse von Hund hinterlegt werden
        super(Hund, self).__init__(rasse, geschlecht, alter)
        self.zahl_beine = zahl_beine

    #Funktionsertweiterung
    def printRasse(self):
        super().printRasse()
        print('(Hund) Rasse: ', self.rasse) #Fkt. wird überschrieben, wenn beide ausführen, dann wieder mit super()
        



hund_1 = Hund(4, 'Bordercollie', 'm', 10)
hund_1.printRasse()