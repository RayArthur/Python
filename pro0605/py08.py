def f1(a, b):
    return a + b

def f3():
    print('Python')

def f5(a=1, b=2, c=3):
    return a + b + c

def f7(x, y):
    if x > y:
        return x
    else:
        return y




print(f1, type(f1))
print(f1(1, 3))
print('-' * 30)

f2 = lambda a, b : a + b #匿名函式
print(f2, type(f2))
print(f2(3, 5))
print(f2(2, 6))
print('-' * 30)

f3()

f4 = lambda  : print('Python...')
f4()

print('-' * 30)
print(f5(1, 3, 5))

f6 = lambda a=1, b=2, c=3 : a + b + c
print(f6())
print(f6(3))

print('-' * 30)

# x = input('x=')
# y = input('y=')

x, y = [int(i) for i in input('輸入 x,y = ').split(',')]
print(x, type(x))
print(y, type(y))
print(f'{x} 和 {y} 最大值：{f7(x, y)}')

#print(f'{x} 和 {y} 最大值：{f7(int(x), int(y))}')
print('-' * 30)

b = []
a = input('輸入 x,y = ').split(',')
for i in a:
    b.append(int(i))

x, y = b
print(x, type(x))
print(y, type(y))
print(f'{x} 和 {y} 最大值：{f7(x, y)}')

f8 = lambda x, y : x if x<y else y
print(f'{x} 和 {y} 最小值：{f8(x, y)}')


