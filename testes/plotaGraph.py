print "Hello World!"
print "Hello Again"
print "I like typing this."
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 1, num=100)

y = x
plt.plot(x, y, 'r--')
z = [t**2 for t in x]
plt.plot(x, z, 'bo')
w = [t**3 for t in x]
plt.plot(x, w, 'g^')
plt.show()
