a, b, c = 4, 2, 5
d, f = 3.25, 5.5

print(f'a={a}, b={b}, c={c}')

# + - * / %(餘數) // **
print('a * b =', a * b)
print('a ** b =', a ** b)
print('a % 3 =', a % 3)
print('c / b =', c / b)
print('c // b =', c // b)
print('d + f =', d + f)

print('-' * 30)

print(0.1 + 0.1 + 0.1)
print(1.0 - 0.8)

print('-' * 30)

r = 30.17
NTD = int(input('輸入台幣：'))
USD = NTD / r
print(f'兌換美元：{USD:.2f}')

# 指派運算
# += -= *= /= %= **= //=
# a = a + b
# a += b
money = int(input('輸入台幣：'))
# money = money / r
money /= r
print(f'兌換美元：{money:.2f}')

print('-' * 30)

# 關係運算
# > >= < <= ==(相等) !=(不相等)  ---> True / False
a = 5
b = 3
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)
print(a == b)
print(a != b)

# 邏輯運算
# and(且)：a and b
# or(或)： a or b
# not(反)： not a
a = 2
b = 3
c = 4
boo = (a + 2) > (b + 3) or (c + 4) > (b - 2)
print('boo:', boo)
print('not boo：', not boo)

print('-' * 30)


a = 5
b = 5
c = 5.0
# is(比 == 更嚴格，資料型別必須相同)
print('a == b：', a == b)
print('a is b：', a is b)

print('a == c：', a == c)
print('a is c：', a is c)

# is not(比 != 更寬鬆，資料型別不同就當作不相等
print('a != b：', a != b)
print('a is not b：', a is not b)

print('a != c：', a != c)
print('a is not c：', a is not c)








