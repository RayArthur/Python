import numpy as np

np_a = np.arange(10) * 10
print(np_a)

print(np_a[3])
print(np_a[:5])
print(np_a[5:])
print(np_a[3:7])
print(np_a[1:7:2])
print(np_a[5:1:-1]) # [50 40 30 20]
print(np_a[:])
print(np_a[:-1])
print(np_a[::-1])

print('-' * 30)

np_b = np.arange(1, 17)
print(np_b)

np_b = np.arange(1, 17).reshape(4, 4)
print(np_b)
print(np_b[2])
print(np_b[2:])
print(np_b[1:3])
print(np_b[1:3, 1:3])
print(np_b[:, 1:3])
print(np_b[1, :])
print(np_b[1])

print('-' * 30)

np_c = np.array([[ 0,  1,  2,  3,  4,  5],
                 [10, 11, 12, 13, 14, 15],
                 [20, 21, 22, 23, 24, 25],
                 [30, 31, 32, 33, 34, 35],
                 [40, 41, 42, 43, 44, 45],
                 [50, 51, 52, 53, 54, 55],])
print(np_c)

np_c = np.array([0, 1, 2, 3, 4, 5] * 6).reshape(6, 6)
print(np_c)

for i in range(1,6):
    np_c[i] = np_c[i] + i * 10

print(np_c)
print(np_c[0, 3:5])
print(np_c[4:, 4:])
print(np_c[:3, :3])
print(np_c[:, 2])
print(np_c[(0, 1, 2, 3, 4), (1, 2, 3, 4, 5)])
print(np_c[3:, 0:6:2])
print(np_c[3:, [0, 2, 5]])



