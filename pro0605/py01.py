a = 10
b = 5
c = 12

list1 = [10, 5, 12]
print(list1, type(list1))
# 取值
print('list1[2]：', list1[2])
# 設值
list1[0] = 20
print(list1)

for i in list1:
    print('%d  ' % i, end='')

print()
print('-' * 30)

tuple1 = (10, 5, 12)
print(tuple1, type(tuple1))
# 取值
print('tuple1[2]：', tuple1[2])
# 設值
# tuple1[0] = 20 # 不可以修改
# print(tuple1)

temp = list(tuple1)
print(temp, type(temp))
temp[0] = 20
tuple1 = tuple(temp)
print(tuple1, type(tuple1))

for i in tuple1:
    print('%d  ' % i, end='')

print()
print('-' * 30)

# list附加資料
list2 = [123, 'ABC', 456]
list2.append('DEF')
print(list2)

list3 = [123, 456]
list4 = ['ABC', 'DEF']

list3.append(list4)
print(list3) #[123, 456, ['ABC', 'DEF']]    [123, 456, 'ABC', 'DEF']

list3.extend(list4)
print(list3)

list5 = [1, 2, 3]
print('list5：', list5, 'id：', id(list5))
list6 = [4, 5]
list5.append(list6)
print('list5：', list5, 'id：', id(list5))

list7 = [2, 3, 4]
print('list7：', list7, 'id：', id(list7))
list8 = [5, 6]
list7 += list8
print('list7：', list7, 'id：', id(list7))

list9 = [3, 4, 5]
print('list9：', list9, 'id：', id(list9))
list10 = [6, 7]
list9.extend(list10)
print('list9：', list9, 'id：', id(list9))

print('-' * 30)

list9.insert(1, 'python')
print('list9：', list9, 'id：', id(list9), 'size：', len(list9))
list9.insert(88, 'java')
print('list9：', list9, 'id：', id(list9), 'size：', len(list9))

list9.remove(4)
print('list9：', list9, 'id：', id(list9), 'size：', len(list9))

# list9.remove(50)
if 50 in list9:
    list9.remove(50)
else:
    print('Error!')
print('list9：', list9, 'id：', id(list9), 'size：', len(list9))

list9.pop(5)
print('list9：', list9, 'id：', id(list9), 'size：', len(list9))

# list9.pop(30)
if 30 < len(list9):
    list9.pop(30)
else:
    print('Error!')
print('list9：', list9, 'id：', id(list9), 'size：', len(list9))

print('-' * 30)
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(list1[3])
print(list1[2:6])
print(list1[:5])
print(list1[5:])

del list1[3]
del list1[3:6]
print(list1)

list2 = [1, 3, 5, 7, 9, 2, 4, 6, 8]
print('# ', list2)
# sorted()
sorted(list2)
print('@ ', list2)
print('@@ ', sorted(list2))
print('@@@ ', sorted(list2, reverse=True))

# list.sort()
print('# ', list2)
list2.sort()
print('@ ', list2)
list2.sort(reverse=True)
print('@@ ', list2)

print('-' * 30)

list3 = [99, 88, 77, 66, 99, 90, 75, 99,  95]
print(max(list3))
print(min(list3))
print(sum(list3))
print(list3.count(99))
print(list3.index(77))
list3.reverse()
print(list3)