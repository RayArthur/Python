import numpy as np

data = np.array([611,566,678,877,1252,1500,1549,1636,1732,1602,1836,2232,2218,2072,1243,905,695,390,183,38,4])
print(data)
print()
print(np.sort(data))
print(np.argsort(data))
print('-' * 30)
print(data)

for i in np.argsort(data):
    print(data[i], end=' ')

print()
print('-' * 30)

# data = np.sort(data)
# data.sort()
data = sorted(data)
print(data)
print(type(data))

print('-' * 30)

np.random.seed(1000)
data = np.random.randint(0, 10, (3, 5))
print(data)

print(np.sort(data, axis=0))
print(np.sort(data, axis=1))



