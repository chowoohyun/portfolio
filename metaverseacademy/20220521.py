
# path = 'C:\\Users\\ChO\\Desktop\\Workplace\\metaverseacademy\\note.txt'

# open(path, 'r')


# import os

# os.path.exists(path)

import numpy as np

# import pandas as pd

import matplotlib.pyplot as plt


# myset ={
#      'A': 1.0,
#      'B': pd.Series(2, index=list(range(5,8))),
#      'C': np.array([3]*3, dtype=float)}
 

# df = pd.DataFrame(myset)

# print(df)


x =np.array([1, 3, 5, 7, 9])

y = x ** 2

plt.plot(x, y, 'oy-' )

plt.show()