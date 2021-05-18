import numpy as np
from scipy.constants import pi
import matplotlib.pyplot as plt
theta = np.asfarray(range(-50, 51)) / 50 * pi
no = 1.8
ne = 1.25
def ne_t(no, ne, theta):
    ne_theta = []
    for i in theta:
        ne_theta.append(1/np.sqrt(np.sin(i)**2/ne**2 + np.cos(i)**2/no**2))
        #ne_theta.append(no * np.sqrt((1 + np.tan(i) ** 2) / (1 + (no / ne) ** 2 * np.tan(theta) ** 2)))
    return np.array(ne_theta)


ne_theta = ne_t(no, ne, theta)
no = np.ones((1,101))*no
print(no)
print(ne_theta)
plt.polar(theta, ne_theta, theta, no[0])
plt.legend("eo")
plt.show()
