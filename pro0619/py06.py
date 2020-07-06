import numpy as np

# [8397,8393,8389,8376,8378,8395,8411,8409,8406,8413,8408,8408,8414,8421,8411,8392,8404]
sales = np.array([8397, 8393, 8389, 8376, 8378, 8395, 8411, 8409, 8406, 8413, 8408, 8408, 8414, 8421, 8411, 8392, 8404])

month = 1
for count in sales:
    if month > 12: #109
        print('民國109年{:2d}月銷售:{}'.format(month - 12, count))
    else: # 108
        print('民國108年{:2d}月銷售:{}'.format(month, count))
    month = month + 1

print('最大值為：', np.max(sales))
print('最小值為：', np.min(sales))
print('中位數為：', np.median(sales))
print('平均值為：', np.mean(sales))
