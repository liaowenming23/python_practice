import csv

with open('/Users/liaowenming/Projects/Python/Practice/data_a.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    arr = {}
    for row in csv_reader:
        arr[row[0]] = row[1]
        
for a in arr:
    print(a + ' value ' + arr[a])
