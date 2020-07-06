dict1 = {'a': 100, 'b': 200, 'c': 300}
print(dict1, type(dict1))

dict1 = {'a': 100, 'b': 200, 'b': 300}
print(dict1, type(dict1))

# 取值
print(dict1['a'])
#print(dict1['c']) # key 不存在同會產生錯誤 --> KeyError: 'c'

print('dict1.get("a")：', dict1.get('a'))
print('dict1.get("aa")：', dict1.get('aa'))

print('dict1.setdefault("a")：', dict1.setdefault('a'))
print('dict1.setdefault("aa")：', dict1.setdefault('aa'))
print("%% ", dict1)

# 設值
dict1['a'] = 150
print(dict1)

dict1['c'] = 300  # key 不存在同 update() 新增
print(dict1)

dict1.update({'d': 400, 'e': 500})
print(dict1)

del dict1['c']
print('# ', dict1)

dict1.clear()
print('@ ', dict1)

del dict1
# print('@ ', dict1)

print('-' * 30)

dict2 = {'a': 100, 'b': 200, 'c': 300, 'd': 400, 'e': 500}
print(dict2)
print(dict2.keys())
print(dict2.values())
print(dict2.items())

for k in dict2.keys():
    print(k, end=' | ')
print()

for k in dict2:
    print(k, end=' | ')
print()

for v in dict2.values():
    print(v, end=' | ')
print()

for k, v in dict2.items():
    print(k, '-->', v)


