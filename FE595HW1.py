import math
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,2*math.pi,1000)
y = np.sin(x)
y0 = np.cos(x)

if __name__ == "__main__":
	plt.plot(x,y)
	plt.show()
	plt.plot(x,y0)
	plt.show()
