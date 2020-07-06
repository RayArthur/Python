import os

print(os.getcwd())

text = '''Python 3.8
程式開發：
1. Python
2. Java
3. C#
4. T-SQL'''

print(text)
print(text, file=open('data1.txt', 'w', encoding='utf8'))

file = open('data2.txt', 'w', encoding='utf8')
file.write(text)
file.close()

print('-' * 30)

file = open('data2.txt', 'r', encoding='utf8')

print('## 1.', file.tell())
text2 = file.read()
print(text2)
print(type(text2))
print('## 2.', file.tell())

print('=' * 30)


file.seek(0, 0)
print('## 3.', file.tell())
text3 = file.read(15)
print(text3)
print('## 4.', file.tell())

print('=' * 30)

file.close()

print('-' * 30)

with open('data2.txt', 'r', encoding='utf8') as file:
    #line = file.read()
    #line = file.readline()
    line = file.readlines()
    print(line, type(line))

for s in line:
    print(s)
    print('-----')


