import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-50,50,1000)

def create_gaussian(t, mean, std):
    g = lambda x : 1/(std*np.sqrt(2*np.pi)) * np.exp(- (x-mean)**2 / (2*std**2))
    return list(map(g,t))


y0 = create_gaussian(x, 0, 10)
y1 = create_gaussian(x, 0, 15)
y2 = create_gaussian(x, 0, 20)

plt.plot(x, y0)
plt.plot(x, y1)
plt.plot(x, y2)
plt.grid()
plt.show()

# I add this line
# And this line
