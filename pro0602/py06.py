# range(結束值)
a = range(5)
print(a)
print(list(a))  # [0, 1, 2, 3, 4]

print('-' * 30)
# range(開始值, 結束值)
b: range = range(1, 6)
print(b)
print(list(b))  # [1, 2, 3, 4, 5]

print('-' * 30)
# range(開始值, 結束值, 間隔值)
c = range(1, 9, 2)
print(c)
print(list(c)) # [1, 3, 5, 7]

print('-' * 30)
# for 變數 in range():
#     程式區塊

for i in range(2, 15, 3):
    print('%3d' % i, end='')
print(', i 結束時 i =', i)

print('-' * 30)
for i in range(10, -1, -2):
    print('%3d' % i, end='')
print('\n------------------------------')

total = 0
for i in range(1, 51):
    # if i % 5 != 0:
    #     print('%3d' % i, end='')
    if i % 5 == 0:
        continue
    print('%3d' % i, end='')
    total = total + i
    if total > 300:
        break

print('\ntotal =', total)
print('------------------------------')

for i in range(1, 10):
    print(i)
    if i % 3 == 0:
        break
else:
    print('OVER')

print('------------------------------')
n = int(input('輸入大於 1 的整數：'))
if n == 2:
    print('2 是質數')
else:
    for i in range(2, n):
        if n % i == 0:
            print('%d 不是質數!' % n)
            break
    else:
        print('%d 是質數!' % n)

print('------------------------------')
for i in range(2, 10):
    for j in range(1, 10):
        print('%dX%d=%2d' % (i, j, i*j), end='\t')
    print('')
print('------------------------------')
for i in range(1, 10):
    for j in range(2, 10):
        print('%dX%d=%2d' % (j, i, i*j), end='\t')
    print('')
print('------------------------------')
print()
print(' x |', end='')
for i in range(2, 10):
    print('%3d ' % i, end='')
print()
for i in range(1, 37):
    if i == 4:
        print('+', end='')
    else:
        print('-', end='')
print()
for i in range(1, 10):
    print(' %d |' % i, end='')
    for j in range(2, 10):
        print('%3d ' % (i*j), end='')
    print('')