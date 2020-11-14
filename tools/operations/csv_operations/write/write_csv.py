import csv

with open('file.csv', 'w') as f:
    writer = csv.writer(f)
    writer.writerow(['TEST1', 'TEST2', 'TEST3'])
