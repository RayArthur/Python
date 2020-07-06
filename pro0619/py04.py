import numpy as np

np_a = np.array([[1, 2, 3], [4, 5, 6]])
print(np_a)
print(np_a.shape)
print('-' * 30)
np_b = np_a.reshape(3, 2)
print(np_b)
print(np_b.shape)
print('-' * 30)
np_b[1, 0] = 30

print(np_a)
print(np_b)
# print('-' * 30)
# np_c = np_a.reshape(4, 5)
# print(np_c)
# print(np_c.shape)

print('=' * 50)
np_a = np.array([[1, 2, 3], [4, 5, 6]])
print(np_a)
print(np_a.shape)
print('-' * 30)
np_b = np.resize(np_a, (3, 2))
print(np_b)
print(np_b.shape)
print('-' * 30)
np_b[1, 0] = 30

print(np_a)
print(np_b)
print('-' * 30)

np_c = np.resize(np_a, (4, 5))
print(np_c)
print(np_c.shape)