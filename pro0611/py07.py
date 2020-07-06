import json

data = {}

with open('aqi.json', 'r', encoding='utf8') as file:
    data = json.load(file)

county = input('輸入查詢縣市：')

print('{:6s}{:12s}{:8s}{:8s}{:8s}'.format('測站編號', '測站名稱', '空氣品質指標', '狀態', 'PM2.5'))
for row in data:
    if row['County'] == county:
        print('{:9s}{:13s}{:11s}{:8s}{:10s}'.format(row['SiteId'], row['SiteName'], row['AQI'], row['Status'], row['PM2.5']))