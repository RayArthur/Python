a = 'Python'
b = 3.8
print(a + str(b))

print(a, b)
print(a, b, sep='')
print(a, b, sep='---')
print(1, '2', 3, 4, 5)
print(1, '2', 3, 4, 5, sep=' --> ')

print('-' * 30)

print('abc')
print('def')
print(123)

print('-' * 30)

print('abc', end='')
print('def', end='')
print(123)

print('-' * 30)

print('abc\ndef\n123')

print('-' * 30)

print('python', end=' ')
print('版本v', 3.8, sep='', end=' ')
print(800, end=' ')
print('元')

print('python 版本v3.8 800 元')

print('-' * 30)

name = 'Amy'
age = 10
height = 135.7

print('我是 Amy，今年 10 歲，身高 135.7 公分')
print('我是 ' + name + '，今年 ' + str(age) + ' 歲，身高 ' + str(height) + ' 公分')
print('我是 ', name, '，今年 ', age, ' 歲，身高 ', height, ' 公分', sep='')
print('我是 %s，今年 %s 歲，身高 %s 公分' % (name, age, height))
print('我是 %s，今年 %o 歲，身高 %.2f 公分' % (name, age, height))

s = '我是 %s，今年 %s 歲，身高 %s 公分' % (name, age, height)
print(s)

print('-' * 30)
print('我是 %s' % name)

a = 5566
print('%d' % a)
print('%i' % a)
print('%o' % a)
print('%x' % a)
print('%X' % a) #0-9 A(10) B(11) C(12) D(13) E(14) F(15)
print(a)

b = 123.4567
print('%f' % b)
print('%.2f' % b)

print('%6.2f' % 123.456789)
print('%6.2f' % 12.3456789)
print('%6.2f' % 1.23456789)

print('-' * 30)

c = 123
print('|%d|' % c)
print('|%10d|' % c)
print('|%-10d|' % c)
print('|%+10d|' % c)
print('|%-+10d|' % c)
print('|%+-10d|' % c)

print('-' * 30)

c = 'python'
print('|%s|' % c)
print('|%10s|' % c)
print('|%-10s|' % c)

print('-' * 30)

print('%5s%6s%6s' % ('名字', '國文', '英文'))
print('%6s%7.1f%7.1f' % ('Amy', 95.6, 80.0))
print('%6s%7.1f%7.1f' % ('Tom', 100.0, 90.2))
print('%6s%7.1f%7.1f' % ('Jackie', 99.9, 88.8))

print('-' * 30)
p_type = 'A'
print('%s%04d' % (p_type, 1))
print('%s%04d' % (p_type, 25))
print('%s%04d' % (p_type, 168))
print('%s%04d' % (p_type, 2266))


'''
{:d}        : 整數
{:f}        : 浮點數
{:e} {:E}   : 科學記號
{:x} {:X}   : 十六進位
{:o}        : 八進位
{:b}        : 二進位
{:%}        : 以百分比的方式輸出
'''

name = 'Amy'
age = 10
height = 135.7

print('我是 Amy，今年 10 歲，身高 135.7 公分')
print('我是 {}，今年 {} 歲，身高 {} 公分'.format(name, age, height))

print('{2} {0} {2} {1}'.format(name, age, height))

print('{:.1%}'.format(0.75))

print('-' * 30)

print('{}{:04d}'.format('A',1))
print('{}{:04d}'.format('B',25))
print('{}{:04d}'.format('C',168))
print('{}{:04d}'.format('D',2266))

print('{1:04d}'.format('A',1))
print('{1:04d}'.format('B',25))
print('{1:04d}'.format('C',168))
print('{1:04d}'.format('D',2266))

print('-' * 30)

# f-string
import sys
version = sys.version

l_name = 'Python'

print(f'我的 {l_name} 版本：{version}')

name = 'Amy'
age = 10
height = 135.7

print(f'我是 {name}，今年 {age} 歲，身高 {height} 公分')

print(f'{height * 2}')
print(f'2**5={2 ** 5}')

a = 123.456789
print(f'{a:.2f}')













