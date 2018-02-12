# Klassen und Vererbung
#
# Aufgabe:
# Erstelle eine Klasse, die dich als mensch darstellt mit den Attributen Name, 
# Nachname, Alter. Schreibe dann eine Funktion, die dir die Daten ausgibt. Erstelle
# weiter eine Klasse Student, die davon erbt und ebenfalls dazu Matrikelnummer, 
# Semester und Studiengang als Attribut besitzt.
#
# Zusatzaufgabe: Erstelle einige Objekte und iteriere über sie. Teste dann bei der
# Iteration, ob das Objekt ein Student ist oder nicht.


# Erstellen der Klasse Mensch

class Mensch:

    name = ''
    nachname = ''
    alter = 0

    def __init__(self, name, nachname, alter):
        self.name = name
        self.nachname = nachname
        self.alter = alter

    def printMensch(self):
        print('Name: ', self.name)
        print('Nachname: ', self.nachname)
        print('Alter: ', self.alter)


# Klasse Student + Vererbung

class Student(Mensch):

    matrikelnummer = 0000
    semester = 0
    studiengang = ''

    def __init__(self, matrikelnummer, semester, studiengang, name, nachname, alter):
        super().__init__(name, nachname, alter)
        self.matrikelnummer = matrikelnummer
        self.semester = semester
        self.studiengang = studiengang

    def printMensch(self):
        super().printMensch()
        print('Matr. Nr.: ', self.matrikelnummer)
        print('Semester: ', self.semester)
        print('Studiengang: ', self.studiengang)

    

andreas = Student(11044, 6, 'ET', 'Andreas', 'Weidemann', 30)
andreas.printMensch()

# Klassenzugehörigkeit

print('Ist Andreas ein Student?')
if isinstance(andreas, Student):
    print('ja')
else:
    print('nein')


