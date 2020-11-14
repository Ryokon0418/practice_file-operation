import csv

# Create your views here.
# def read_csv():
with open('file.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)
    print(f.read())
