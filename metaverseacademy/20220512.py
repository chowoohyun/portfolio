'''
[AI 전공] 3차시 - 파이썬 기초 문법 (3) 및 라이브러리

'''

#Matplotlib

import matplotlib.pyplot as plt 
import numpy as np

# x = np.array([0, 6])
# y = np.array([0, 250])

# plt.plot(x, y)
# plt.show()

# x1 = np.array([1,8])
# y1 = np.array([3,10])

# plt.plot(x1, y1, 'o')
# plt.show()

x1 = np.array([1,2,6,8])
y1 = np.array([3,1,8,10])

plt.plot(x1,y1, marker='o')
plt.show()