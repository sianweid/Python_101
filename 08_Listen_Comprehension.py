# Das richtige Anlegen von Listen

vector = [0,0,0,0] #schlecht
print(vector)

vector = [0 for _ in range(4)] #elegant; "_" als Platzhalter, s.d. keine Variable erzeugt werden muss
print(vector)

vector = [i for i in range(10)]
print(vector)




# optional Vector-Generator

vec_gen = (i for i in range(10))
vector = [val for val in vec_gen]
print (vector)



# Matrix (2d Liste) anlegen

matrix = [ [1,0], [0,1] ]
print(matrix)

matrix = [[0 for j in range(4)] for i in range(3)]  # [[spalten]zeilen] => innere Klammer Spalten, äußere Zeilen
print(matrix)

matrix = [[i*j for j in range(4)] for i in range(3)]
print(matrix)