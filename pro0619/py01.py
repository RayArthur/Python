import numpy as np

list_a = [1, 2, 3, 4, 5]
print(list_a[1:4])

list_b = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]
print(list_b[0])
print(list_b[1][2])

list_c = [1, 2, 3, 4, 5]
list_d = [1, 3, 5, 7, 9]
list_e = list_c + list_d
print(list_e, type(list_e))

print(list_c * 2)
print('-' * 30)

np_a = np.array(list_c)
np_b = np.array(list_d)
print(np_a, type(np_a))
print(np_a.shape)

np_c = np_a + np_b
print(np_c, type(np_c))
print(np_a * 2)

# bool -> int -> float -> str
list_f = [True, True, False,  True, 5, 6.2, 'abc']
np_d = np.array(list_f)
print(np_d)

print('-' * 30)

np_a = np.array([1, 2, 3, 4])
print(np_a, type(np_a))
print('維度數量：', np_a.ndim)
print('形狀：', np_a.shape)
print('元素數量：', np_a.size)
print('元素型態：', np_a.dtype)

np_b = np.array(((1, 3, 5, 7), (2, 4, 6, 8)))
print(np_b, type(np_b))
print('維度數量：', np_b.ndim)
print('形狀：', np_b.shape)
print('元素數量：', np_b.size)
print('元素型態：', np_b.dtype)

print('-' * 30)

print(np.empty((2, 4)))
print(np.zeros((3, 4)))
print(np.ones((5, 2)))
print(np.full((4, 3), 6))
print(np.eye(4))
print(np.diag([1, 2, 3, 4]))

print('-' * 30)

for i in range(5, 30, 2):
    print(i, end=' ')
print()

np_a = np.arange(5.0)
print(np_a, type(np_a), np_a.dtype)

np_a = np.arange(5, 15)
print(np_a, type(np_a), np_a.dtype)

np_a = np.arange(6, 30, 3)
print(np_a, type(np_a), np_a.dtype)

np_a = np.arange(6, 30, 2.5)
print(np_a, type(np_a), np_a.dtype)

np_b = np.linspace(1, 10)
print(np_b, type(np_b), np_b.dtype)

np_b = np.linspace(1, 10, 10 )
print(np_b, type(np_b), np_b.dtype)

np_b = np.linspace(1, 10, 10 , endpoint=False)
print(np_b, type(np_b), np_b.dtype)

np_b = np.linspace(1, 10, 11)
print(np_b, type(np_b), np_b.dtype)

print('-' * 30)

print(np.random.rand(2, 3))
print(np.random.randn(2, 3))
print(np.random.randint(10))
print(np.random.randint(2, 10, [6]))
print(np.random.random(4))

