import json

json1 ='{"student": [{"id": "S01", "name": "小明", "score": 95, "pass": true, "notes": null}, {"id": "S02", "name": "tom", "score": 59, "pass": false, "notes": "Python"}]}'
print('json1：', json1)

dict1 = json.loads(json1)
print('dict1：', dict1)

print('--------------')

dict2 = {}
with open('scores.json', 'r', encoding='utf8') as file:
    dict2 = json.load(file)

print('dict2：', dict2)
print('--------------')

for s in dict2['student']:
    print('id：', s['id'])
    print('name：', s['name'])
    print('score：', s['score'])
    print('pass：', s['pass'])
    print('notes：', s['notes'])
    print('-------------------')
