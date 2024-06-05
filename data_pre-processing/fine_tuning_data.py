import json


# 读取JSON文件
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


# 找到最佳算法
def find_best_algorithm(runs):
    best_algorithm = None
    min_runtime = float('inf')
    for run in runs:
        try:
            run_runtime = float(run['runtime'])  # 将字符串转换为浮点数
        except (ValueError, TypeError) as e:
            print(f"Error converting runtime to float for {run}: {e}")
            continue
        if run['runstatus'] == 'ok' and run_runtime < min_runtime:
            best_algorithm = run['algorithm']
            min_runtime = run_runtime
    return best_algorithm


# 处理数据并生成新JSON格式
def process_data(feature_values, feature_runs):
    output_data = []  # 存储每条转换后的数据
    index = 0  # 添加索引以追踪feature_runs的位置
    for feature in feature_values:
        # 每次处理8条记录，如果不足8条，则处理剩余的所有记录
        runs_subset = feature_runs[index:min(index + 8, len(feature_runs))]
        best_algorithm = find_best_algorithm(runs_subset)
        if best_algorithm:
            assistant_content = f'算法选择结果：{best_algorithm} | 选择依据：首先分析本问题在该算法的执行结果中执行状态为ok，其次在所有执行状态为ok的算法中选择执行时间最短的算法。'
        else:
            assistant_content = '未找到合适的算法。'

        data = {
            "conversations": [
                {
                    "role": "user",
                    "content": f"问题特征：{json.dumps(feature, ensure_ascii=False)}，问题在算法上的执行结果：{json.dumps(runs_subset, ensure_ascii=False)}"
                },
                {
                    "role": "assistant",
                    "content": assistant_content
                }
            ]
        }
        output_data.append(data)
        index += 8  # 更新索引以指向下一组8条记录的开始位置

    return output_data


# 读取数据
feature_values = read_json_file('feature_values.json')
feature_runs = read_json_file('algorithm_runs.json')  # 确保文件名正确

# 处理数据
new_data = process_data(feature_values, feature_runs)

# 写入新JSON文件，每条数据独占一行
with open('test.json', 'w', encoding='utf-8') as file:
    for data in new_data:
        json.dump(data, file, ensure_ascii=False)
        file.write('\n')  # 添加换行符以分隔每条数据
