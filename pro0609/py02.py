import ast

no = 1
scores = {}

while True:
    score = int(input('輸入 No' + str(no) + ' 成績(-1結束)：'))
    if score == -1: break
    scores[no] = score
    no += 1

print(scores)

file = open('score.txt', 'w', encoding='utf8')
file.write(str(scores))
file.close()

print('-' * 30)

scores2 = {}
with open('score.txt', 'r', encoding='utf8') as file:
    data = file.read()
    print(data, type(data))
    scores2 = ast.literal_eval(data)
    print(scores2, type(scores2))

print(sum(dict(scores2).values()))
print(sum(scores2.values()))


