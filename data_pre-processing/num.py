from collections import Counter


def count_total_characters(filename):
    # 初始化字符计数器
    total_chars = 0

    # 打开并读取文件
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            # 将每行的字符数累加到总数中
            total_chars += len(line)

    # 返回总字符数
    return total_chars


# 调用函数并传入文件名
filename = 'text.txt'  # 请替换为你的文件名
total_character_count = count_total_characters(filename)

# 打印总字符数
print(f"字符总数: {total_character_count}")
