# 在index的caption后中加入新的文件
import os

def add_filenames(directory, string_incoulded, target_position):
    all_file=target_position+"\n"
    for filename in os.listdir(directory):
        if string_incoulded in filename:
            add_file = os.path.join(directory, filename)
            all_file = all_file+"\n   "+add_file
    with open("index.rst", 'r') as file:
        filedata = file.read()
    filedata = filedata.replace(target_position, all_file)
    with open("index.rst", 'w') as file:
        file.write(filedata)


def delete_lines_with_string(file_path, string):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    with open(file_path, 'w') as file:
        add_newline = False  # 标记是否需要添加空行
        for line in lines:
            if string not in line:
                if line.strip():  # 排除空行
                    file.write(line)
                else:
                    add_newline = True  # 标记下一行需要添加空行
            elif add_newline:
                file.write('\n')  # 在删除行后的位置添加空行
                add_newline = False  # 重置标记


# 指定目录路径
directory1 = '1qiskit'
directory2 = '2transline'
directory3 = '3chip'
directory4 = '4heatload'
directory5 = '5qubit'

# 文件名字包含的字符
string_incoulded = ".md"

# 指定目标字符串
target_position1 = '   :caption: QISKIT'
target_position2 = '   :caption: TRANS-LINE'
target_position3 = '   :caption: CHIP'
target_position4 = '   :caption: HEAT-LOAD'
target_position5 = '   :caption: QUBIT'

# 删除包含'md'的行
delete_lines_with_string('index.rst', 'md')

# 调用函数进行替换
add_filenames(directory1, string_incoulded, target_position1)
add_filenames(directory2, string_incoulded, target_position2)
add_filenames(directory3, string_incoulded, target_position3)
add_filenames(directory4, string_incoulded, target_position4)
add_filenames(directory5, string_incoulded, target_position5)

def add_empty_line_before_string(file_path, string):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        found_string = False  # 标记是否找到指定字符串
        for line in lines:
            if string in line:
                if not found_string:
                    file.write('\n')  # 在找到的字符串前添加一个空行
                found_string = True  # 找到指定字符串，标记为True
            file.write(line)

add_empty_line_before_string('index.rst', 'Quantum Computing Learning')


def add_empty_line_after_string(file_path, string):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    with open(file_path, 'w') as file:
        found_string = False  # 标记是否找到指定字符串
        for line in lines:
            file.write(line)
            if string in line:
                found_string = True  # 找到指定字符串，标记为True
                file.write('\n')  # 在找到的字符串后添加一个空行

    if not found_string:
        print("未找到指定字符串。")

add_empty_line_after_string('index.rst', '=======================================')

