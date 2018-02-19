# Global and Local Variables
# Global: Überall zugreifbar
# Local: Nur in seinem Frame/Environment verwendbar


x = 6
# noch KEINE globale Variable, aber in Funtkionen verwendbar (außer Rechenoperationen, in denen x überschrieben wird)

def example():
    z = 5
    print(z)

example()


def example2():
    
    global x # x zu globaler Variable
    print(x)
    x += 5
    print(x)

    y = x + 20

    return y # über return könenn bei Funktionsaufruf Variablenwerte im "Mainloop" überschrieben werden

y = example2()
print (y)

