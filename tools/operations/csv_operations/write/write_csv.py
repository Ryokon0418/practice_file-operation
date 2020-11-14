import csv

# 1行分出力
# with open('file.csv', 'w') as f:
#     writer = csv.writer(f)
#     writer.writerow(['TEST1', 'TEST2', 'TEST3'])

# 複数行出力
rows = []
with open('file.csv', 'w') as f:
    writer = csv.writer(f)
    rows = [['ミッフィー', 'ディズニー', '鬼滅'], [
        'ミッフィー', 'ミッキー', 'たんじろう'], ['スナッフィー', 'ミニー', 'ねづこ'], ['ダーン', 'ドナルド', 'いのすけ']]
    writer.writerows(rows)
