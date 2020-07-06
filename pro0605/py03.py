def fun1():
    print('Hello!')

def fun2():
    return 'python '

def fun3(a, b):
    x = a
    y = b
    print(x * y)

def fun4(x, y):
    a = x + y
    b = x - y
    c = x * y
    d = x / y
    return a, b, c, d

def fun5(max):
    # print('1 + ... +', max, '=', sum(list(range(1, max+1))))
    total = 0
    for i in range(1, max + 1):
        total += i
    print('1 + ... +', max, '=', total)

def fun6(a, b, c=None):
    print(a, b, c)

def fun7(id, name, *nums):
    print(nums, type(nums))
    total = sum(nums)
    print('ID：{}, Name：{}, Scores：{}'.format(id, name, total))


# --------------------------------------

fun1()
fun1()
fun1()

fun2() #做白工
msg = fun2()
print(msg * 3)
print(fun2() + '3.8')


fun3(2, 5)
fun3('Hi ', 3)
# fun3('hi ', 'python')

temp = fun4(9, 3)
print(temp, type(temp))

w, x, y, z = fun4(9, 3)
print(w, x, y, z)

fun5(50)
fun5(100)
fun5(200)

fun6(1, 2, 3)
fun6('Python', 'Java', 'C#')
fun6('python', 3.8)

fun6(c='8', a='Java', b='SE')

fun7(1, 'Amy', 90, 80, 70)
fun7(2, 'Jackie', 95, 95, 90, 100)
fun7(3, 'Tom', 99, 80)
fun7(4, 'Lisa')



