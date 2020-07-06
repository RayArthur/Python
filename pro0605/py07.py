import mypackage.test2 as test2


print('py07 __main__')
# 呼叫 test2 模組中的 function
test2.func1()

# 建立 class 物件
tp = test2.testpy()
# 呼叫 tp 物件的成員
# 物件名稱.成員名稱
tp.method1()
print('--------------------------')
book = test2.Book('Rython 3.8')
print(book.bookName)
print('--------------------------')
book = test2.Book('')
print(book.bookName)
