import csv
import json

filename = 'D:\\MyProjects\\AAS-LLM\\datasets\\aslib_data\\BNSL-2016\\feature_runstatus.arff'

# 初始化变量
field_names = []
converted_data = []

# 读取ARFF文件头部以获取字段名
with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter=',', skipinitialspace=True)
    for row in reader:
        # 检查是否是字段定义行
        if row and row[0].startswith('@ATTRIBUTE'):
            # 提取字段名，字段名和类型之间用空格分隔
            field_name = row[0].split()[1]  # 取第一个单词作为字段名
            field_names.append(field_name)

# 读取数据部分并创建字典
with open(filename, 'r') as file:
    reader = csv.reader(file, delimiter=',', skipinitialspace=True)
    # 跳过头部直到遇到@DATA
    for line in reader:
        if line and line[0] == '@DATA':
            break
    # 读取数据行并创建字典
    for row in reader:
        if not row:  # 跳过空行
            continue
        # 确保数据行有足够多的元素
        if len(row) < len(field_names):
            continue  # 或者可以在这里打印一条错误消息
        # 创建字典，映射字段名到对应的值
        data_dict = {field_name: row[i] for i, field_name in enumerate(field_names)}
        # 将字典添加到转换后的数据列表中
        converted_data.append(data_dict)

# # 将转换后的数据转换为JSON格式
json_data = json.dumps(converted_data, ensure_ascii=False)

# # 打印JSON数据，每组数据一行
# print(json_data)

# 将转换后的数据保存到文件，每组数据一行
with open('feature_runstatus.json', 'w', encoding='utf-8') as json_file:
    json_file.write(json_data)
