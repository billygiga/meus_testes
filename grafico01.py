import matplotlib.pyplot as plt
import numpy as np
import math

x = np.linspace(1,2,15)
y = [math.cos(math.radians(i)) for i in x]

plt.figure(dpi=120,facecolor='#b0c4de')
plt.plot(x,y,color='c')
plt.xlabel('populacao')
plt.ylabel('mortalidade')
plt.show()
