def fun1():
    print('fun1()...')
    a = 6 # 區域變數
    print('A.', a)
    a = a + 5
    print('B.', a)

def fun2():
    print('fun2()...')
    global a
    print('A.', a)
    a = a + 5
    print('B.', a)

a = 10 #全域變數

print('__main__')
print('1.', a)
fun1()
print('2.', a)
fun2()
print('3.', a)
a = a * 2
print('4.', a)
