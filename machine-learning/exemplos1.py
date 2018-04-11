import numpy as np
# resolve um sistema de equacoes
# 7x + 5y -3z = 16
# 3x - 5y + 2z = -8
# 5x + 3y - 7z = 0
a = np.array([[7,5,-3], [3,-5,2],[5,3,-7]])
b = np.array([16,-8,0])
x = np.linalg.solve(a, b)
print x
# [ 1.  3.  2.]
