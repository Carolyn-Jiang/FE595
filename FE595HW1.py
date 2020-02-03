import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style

x = np.linspace(0,2*math.pi,1000)
y = np.sin(x)
plt.plot(x,y)
plt.show()

x0 = np.linspace(0,2*math.pi,1000)
y0 = np.cos(x)
plt.plot(x0,y0)
plt.show()