import csv

file = open('example1.csv', 'r', encoding='utf8')

for row in csv.reader(file):
    # print(row)
    if float(row[5]) > 100:
        print(row[0])

file.close()

print('-' * 30)

file = open('example.csv', 'r', encoding='utf8')

for row in csv.DictReader(file):
    # print(row)
    if float(row['漲跌點數']) > 100:
        print(row['日期'])