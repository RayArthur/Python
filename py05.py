a = 5
while a >= 0:
    print(a)
    a -= 1

print('-' * 30)

gender = True
while gender:
    gender = int(input('性別 1)男  2)女  0)結束：'))
    if (gender == 1) or (gender == 2):
        print('男' if gender==1 else '女')
    else:
        print('輸入性別錯誤，重新選擇!')
print('結束!')

print('-' * 30)

while True:
    gender = input('性別 1)男  2)女  0 或 <Enter>)結束：')

    if (gender == '0') or (gender == ''):
        break # 中斷迴圈

    if (int(gender) == 1) or (int(gender) == 2):
        print('男' if int(gender)==1 else '女')
    else:
        print('輸入性別錯誤，重新選擇!')

print('結束!')



