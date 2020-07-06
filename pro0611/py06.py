import json
from urllib import request

url = 'http://opendata.epa.gov.tw/webapi/Data/REWIQA/?$orderby=SiteName&$skip=0&$top=1000&format=json'

print('資料讀取...')
data = request.urlopen(url).read().decode('utf8')
print(data)
# print(json.loads(data))

with open('aqi.json', 'w', encoding='utf8') as file:
    file.write(data)
print('資料儲存成功!')

