# Erstellen von Klassen
# Existieren in Objektorientierten Sprachen
# C hat z.B. keine Klassen, lediglich Strukturen


# Oblekte mit verschiedenen Klassen

class vektor_3d:
    x = 0
    y = 0
    z = 0   # Vektor mit 3 Attributen inkl default Eigenschaften

    def __init__(self, x=0, y=0, z=0): # Contructor            Built-in Functions mit __     self => bezug zur eigenen Instanz
        self.x = x                      # init muss bei klasse definiert werden! klasse muss ansonsten keine weiteren funktionen haben 
        self.y = y
        self.z = z

    def printCoordinates(self):
        print('x: ', self.x)
        print('y: ', self.y)
        print('z: ', self.z)

null_vektor = vektor_3d(0, 0, 0)
null_vektor.printCoordinates()
                                                
