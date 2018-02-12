# Matplotlib Grafiken

import matplotlib.pyplot as plt

data = [1,4,11,8,3]

plt.plot(data, c='r') # Liniendiagramm
plt.scatter(range(len(data)),data, c='b') # Punktdiagramm

# Gerade einzeichnen

x1 = 0
x2 = 5
y1 = 3
y2 = 3

plt.plot((x1,x2),(y1,y2)) # erstes Tupel x, zweites mit y Werten!


plt.xlabel('x-Werte')
plt.ylabel('y-Werte')

plt.show() # Aufruf für Plot

plt.savefig('fig.png') # Speicherbefehl