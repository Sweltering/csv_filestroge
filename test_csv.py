# csv文件处理
import csv


# 读取csv文件，通过下标去读取
def read_csv():
    with open('stock.csv', 'r') as f:
        reader = csv.reader(f)  # 返回一个迭代器
        next(reader)
        for x in reader:
            name = x[3]
            volume = x[-1]
            print({'name': name, 'volume': volume})


# 通过名称去读取
def read_csv2():
    with open('stock.csv', 'r') as f:
        reader = csv.DictReader(f)  # 返回一个迭代器
        for x in reader:
            value = {'name': x['secShortName'], 'volume': x['turnoverVol']}
            print(value)


# 将数据写入到csv文件中, 通过writer写入
def write_csv():
    headers = ['username', 'age', 'height']
    values = [
        ('王杰', 22, 180),
        ('杨子文', 23, 183),
        ('唐波', 21, 175)
    ]

    with open('classroom.csv', 'w', encoding='utf-8', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)  # 写入表头数据
        writer.writerows(values)  # 写入values数据


# 通过字典的方式写入
headers = ['username', 'age', 'height']
values = [
    {'username': "王杰", 'age': 22, 'height': 180},
    {'username': "杨子文", 'age': 23, 'height': 184},
    {'username': "唐波", 'age': 21, 'height': 175}
]
with open('classroom2.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.DictWriter(f, headers)
    writer.writeheader()  # 写入表头数据
    writer.writerows(values)  # 写入values数据

