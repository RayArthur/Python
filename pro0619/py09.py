import numpy as np

data = np.genfromtxt('data3.csv', skip_header=1, delimiter=',', encoding='utf8', unpack=True, dtype='int')
print(data)
print('-' * 30)

total = sum(data[1]) - data[1][0]
print(total)

print('-' * 30)

data1 = np.delete(data, 0, axis=0)
print(data1)
data2 = np.delete(data1, 0, axis=1)
print(data2)
print(data1[0])
print(data2[0])
print(sum(data2[0]))

print('-' * 30)

data = np.genfromtxt('data3.csv', skip_header=1 and 2, delimiter=',', encoding='utf8', unpack=True, dtype='int')
print(data)
print(sum(data[1]))