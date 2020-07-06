import csv

file = open('example.csv', 'r', encoding='utf8')

ex_list = csv.reader(file)
print(ex_list)
print(list(ex_list))

file.seek(0, 0)

outfile = open('out_example.csv', 'w', encoding='utf-8', newline='')

writer = csv.writer(outfile, quotechar='"', quoting=csv.QUOTE_ALL, delimiter=' ')

for row in ex_list:
    writer.writerow(row)

file.close()
outfile.close()

