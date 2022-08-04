'''
This will generate a new file with the merged two columns. 
This will make searching the class alot easier
'''

import csv

with open('DailyEnrollmentReport.csv') as f:
    reader = csv.reader(f)
    with open('newClass.csv', 'w') as g:
        writer = csv.writer(g)
        for row in reader:
            new_row = [''.join([row[0], row[1]])] + row[2:]
            writer.writerow(new_row)
