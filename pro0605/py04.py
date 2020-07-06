def getResult(items):
    max = items[0]
    min = items[0]
    sum = 0
    for i in items:
        if i > max:
            max = i
        if i <min:
            min = i
        sum += i
    return max, min, sum

# ---------------------------
items = []
while True:
    pay = int(input('支出：'))
    if pay==0:
        break
    items.append(pay)
print('----------------------')
max, min, sum = getResult(items)
print('最大：', max)
print('最小：', min)
print('總計：', sum)
print('平均：', sum / len(items))


