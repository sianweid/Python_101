# Latin Hypercube Sampling


import numpy as np
import matplotlib.pyplot as plt

def LatinHypercubeUniform2D(n):        # n = Sampleanzahl
    lowerLimits = np.arange(0, n)/n
    upperLimits = np.arange(1, n+1)/n

    # Uniforme Zufallszahlen generieren

    points = np.random.uniform(low = lowerLimits, high = upperLimits, size = [2, n]).T
    np.random.shuffle(points[:,1])

    return points

n = 100
p =  LatinHypercubeUniform2D(n)

print(p)

plt.figure(figsize=[5, 5])
plt.xlim([0, 1])
plt.ylim([0, 1])
plt.scatter(p[:,0], p[:,1], c = 'r')

plt.show()
     
