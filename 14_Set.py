# Sets (Mengen)
# In sets darf eintrag nur 1x vorkommen!

fam_mutter = {'angelika','klaus','peter'}
fam_vater = {'anne','klaus','gerd'}

print('dieter' in fam_mutter)
print('klaus' in fam_mutter)

fam = fam_mutter | fam_vater
print(fam)

print(fam_mutter & fam_vater) # UND Vergleich

print(fam_mutter ^ fam_vater) # XOR Vergleich

print(fam_mutter - fam_vater) # OR Eintrage der fam-mutter minus der Einträge, die in Schnittmenge vorhanden


# Set Comprehension

familie2 = { person for person in fam_mutter | fam_vater }
print(familie2)

