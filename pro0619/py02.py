import numpy as np

np_a = np.array([2, 4, 6, 8])
np_b = np.arange(4)
print('np_a：', np_a)
print('np_b：', np_b)

np_c = np_a - np_b
print('np_c：', np_c)

np_d = np_b ** 2
print('np_d：', np_d)

np_e = np.array([5, -1, 3, 6, 9, 0])
# print(np_e)
# print(np_e < 5)
# print(np_e[np_e < 5])
# np_e[np_e < 5] = 1
np_e[np_e < 5] = 1
print(np_e)
