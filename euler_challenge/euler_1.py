import numpy as np


a = np.linspace(1, 999, 999)

b = [i for i in a if i % 3 == 0 or i % 5 == 0]
np.sum(b)
