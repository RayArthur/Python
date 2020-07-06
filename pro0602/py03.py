# if 判別式:
#    條件成立時...
# else:
#    條件不成立時...

a = 5
b = 30

if a > b:
    print('a > b')
else:
    print('a < b')

print('-' * 30)

score = int(input('輸入成績：'))

if 0 <= score <= 100:

    '''
    if score >= 60:
        result = '及格'
    else:
        result = '不及格'
    '''

    result = '及格' if score >= 60 else '不及格'

    if score >= 90:
        level = 'A'
    elif score >= 80:
        level = 'B'
    elif score >= 70:
        level = 'C'
    elif score >= 60:
        level = 'D'
    else:
        level = 'F'

    print(f'成績：{score}分，{result}，等級：{level}')

    # print(f'成績：{score}分，{"及格" if score >= 60 else "不及格"}')

else:
    print('成績輸入錯誤!')
