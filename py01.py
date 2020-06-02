# 鍵盤輸入
# 變數名稱 = input('提示文字...')
name = input('輸入名字：')
# age = input('輸入年齡：')
age = int(input('輸入年齡：'))


print(age, type(age))

# print(f'{name}，出生西元：{2020-int(age)}')
print(f'{name}，出生西元：{2020-age}')