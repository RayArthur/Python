import json

dict1 = {'id': 'S01',
         'name': '小明',
         'score': 95,
         'pass': True,
         'notes': None}
dict2 = {'id': 'S02',
         'name': 'tom',
         'score': 59,
         'pass': False,
         'notes': 'Python'}

json1 = json.dumps(dict1, ensure_ascii=False)
print('dict1：', dict1)
print('json1：', json1)

print('----------------')

data = {}
data['student']=[]

print(data['student'], type(data['student']))
print(data)
print('----------------')

data['student'].append(dict1)
data['student'].append(dict2)

print('data：', data)
print('----------------')

json2 = json.dumps(data, ensure_ascii=False)
print('json2：', json2)

print('----------------')

with open('scores.json', 'w', encoding='utf8') as file:
    json.dump(data, file, ensure_ascii=False)