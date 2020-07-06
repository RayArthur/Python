# 單行註解
print('Hello! World!')
print("Hi! python")
print('123"ABC"456')
print("123'ABC'456")

'''
多行註解
可以使用單引號或雙引號3個
'''

"""
多行註解
可以使用單引號或雙引號3個
"""

a = """
多行文字
可以使用單引號或雙引號3個
123
  456
    789
"""
print(a)
print(type(a), id(a))

print('-------------------')

a = 1.23
print(a)
print(type(a), id(a))

print('-------------------')

a = 3 > 5 #3>5 --> True/False
print(a)
print(type(a), id(a))

print('-------------------')

a = 'python'
print(a)
print(type(a), id(a))

print('-------------------')

# a = 'python 3.8'      # + 字串串接符號
# a = 'python' + '3.8'  # + 字串串接符號
# a = a + '3.8'           # + 字串串接符號
a + '3.8'             # + 字串串接符號
# a + 3.8               #會錯誤，字串跟數字不可以直接串接

print(a)
print(type(a), id(a))

print('-------------------')

'''
變數命名規則
第一個字：a-z A-Z _ 中文
第二個字：a-z A-Z 0-9 _ 中文
不可以用關鍵字，使用Python Console 
查看關鍵字：>>> import keyword
          >>> keyword.kwlist   
['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 
 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 'finally', 'for', 
 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 
 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']
          

'''

