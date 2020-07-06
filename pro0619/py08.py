import numpy as np

# data = np.loadtxt('data1.csv') # ValueError: could not convert string to float: 'value1,value2'
# data = np.loadtxt('data1.csv', skiprows=1) # ValueError: could not convert string to float: '0.3,0.1'

data = np.loadtxt('data1.csv', skiprows=1, delimiter=',')
print(data)
print(type(data))

print('-' * 30)

data = np.loadtxt('data1.csv', skiprows=1, delimiter=',', unpack=True)
print(data)

y107, y108 = np.loadtxt('data1.csv', skiprows=1, delimiter=',', unpack=True)
print('y107：', y107, type(y107))
print('y108：', y108, type(y108))

print('-' * 30)

# data = np.loadtxt('data2.csv', skiprows=1, delimiter=',')
data = np.genfromtxt('data2.csv', skip_header=1, delimiter=',')
print(data)
print(type(data))

data = np.genfromtxt('data2.csv', delimiter=',')
print(data)
print(type(data))

np.savetxt('data2_a.csv', data, delimiter=',')
np.savetxt('data2_b.csv', data, delimiter=',', fmt='%1.4f')

data = np.genfromtxt('data2.csv', delimiter=',', filling_values=99)
print(data)
print(type(data))
np.savetxt('data2_c.csv', data, delimiter=',', fmt='%1.4f')
