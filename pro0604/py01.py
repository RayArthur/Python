a = 'python'
print(a)

a = '''abc
123
456'''
print(a)

a = 'Python 3.8'

# [n]
print(a[2], a[-8])

# [n:]
print(a[7:])
print(a[-3:])

# [:m]
print(a[:6])
print(a[:-4])

# [n:m]
print(a[4:8])
print(a[-6:-2])

print('-' * 30)

b = 'This is Python, That is Java, This is SQLite, That is MySQL'
print(b)
print('id：', id(b))
print()

#取代
print('取代：', b.replace('is', '*'))
print(b)
print('id：', id(b))
print()
print('取代：', b.replace('is', '*', 2))
print(b)
print('id：', id(b))
print()

print('-' * 30)
print('0123456789' * 6)
print(b)
print('b.find("Python")：', b.find('Python'))
print('b.find("not")：', b.find('not'))
print('b.find("not")：', b.find('not') if b.find('not') != -1 else '找不到')
print('b.find("is")：', b.find('is'))
print('b.find("is", 20)：', b.find('is', 20))
print('b.find("is", 10, 20)：', b.find('is', 10, 20))

print('-' * 30)
str1 = '-->'
list2 = ['a', 'b', 'c', 'd']
print(str1.join(list2))

print(str1.join('python'))

for s in 'python':
    print(s)

print(list('python'))

print('-' * 30)
print(b)
print(b.split(' '))
print()
print('2020-6-4'.split('-'))

year, month, day = '2020-6-4'.split('-')
print(year)
print(month)
print(day)


str1 = 'abcde'
print(str1)
print(reversed(str1))
print(list(reversed(str1)))

str2 = ''.join(reversed(str1))
print(str2)








