# type()查看變數型別
# id() 查看變數記憶體位置

a = 100
print('a =', a, type(a), id(a))

b = 100
print('b =', b, type(b), id(b))

print('-' * 30)
a = a * 10
print('a =', a, type(a), id(a))
print('b =', b, type(b), id(b))

print('-' * 30)

# 資料型態轉換
a = 5
b = 3.0
c = a + b
print('c =', c, type(c), id(c))

d = False # False->0 True->1
c = a + d
print('c =', c, type(c), id(c))

# 強制轉型：型別(資料)
a = -1
b = 0
c = 1
d = 5
print(bool(a), bool(b), bool(c), bool(d))

a = True
b = False
print(int(a), int(b))

print('-' * 30)

# a = int('123')
# a = int(123.45)
# a = int('234.56') # ValueError: invalid literal for int() with base 10: '234.56'
# a = int('a')      #ValueError: invalid literal for int() with base 10: 'a'
# a = int('abc')      # ValueError: invalid literal for int() with base 10: 'abc'
a = float('234.56')
print('a =', a, type(a), id(a))
a = int(a)
print('a =', a, type(a), id(a))

print('-' * 30)

# a = str(False)
# a = bool('Python') # True
a = bool(None) #空值  # False
print('a =', a, type(a), id(a))




