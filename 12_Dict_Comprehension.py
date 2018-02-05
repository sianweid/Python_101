# Erstellen von Dict Comprehensions (Comp) 

studenten = ['jan', 'peter', 'karl']
noten = [1,1,3]

# Manuelles Zusammenfügen in Dict
stud_dict = {'jan':1,'peter':1,'karl':3}
print(stud_dict)

stud_dict2 = {key: val for key, val in zip(studenten, noten)}
print(stud_dict2)

