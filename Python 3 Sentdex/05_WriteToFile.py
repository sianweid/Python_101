# In Datei schreiben
# Überschreibt Inhalt der Datei

text = 'sampe text to save\nnew line'
saveFile = open('exampleFile.txt','w') # In Klammer kann der Filepath angegeben werde (vor Filename)

saveFile.write(text)

saveFile.close()


# Append()
# append hängt Inhalt an bestehende Datei an

appendMe = '\nNew bit of Information'

appendFile = open('exampleFile.txt','a')
appendFile.write(appendMe)
