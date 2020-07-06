import numpy as np

np_a = np.array([[1, 2, 3], [4, 5, 6]])
print(np_a)
print()

np_b = np.append(np_a, [7, 8, 9])
print(np_b)
print()

np_c = np.append(np_a, [[7, 8, 9]])
print(np_c)
print()

np_d = np.append(np_a, [[7, 8, 9]], axis=0)
print(np_d)
print()

np_e = np.append(np_a, [[7, 8, 9], [9, 8, 7]], axis=1)
print(np_e)
print()

print('-' * 30)

np_a = np.array([[1, 2], [3, 4], [5, 6]])
print(np_a)
print()

np_b = np.insert(np_a, 3, [99, 88])
print(np_b)
print()

np_c = np.insert(np_a, 2, [99, 88], axis=0)
print(np_c)
print()

np_d = np.insert(np_a, 2, [99], axis=0)
print(np_d)
print()

np_e = np.insert(np_a, 2, 99, axis=0)
print(np_e)
print()

np_f = np.insert(np_a, 1, 99, axis=1)
print(np_f)
print()

print('-' * 30)

np_a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np_a)
print()

np_b = np.delete(np_a, 3)
print(np_b)
print()

np_c = np.delete(np_a, 1, axis=0)
print(np_c)
print()

np_d = np.delete(np_a, 1, axis=1)
print(np_d)
print()

