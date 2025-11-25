# coding=utf-8

import yaml
import json
import os
from utils.logger_util import *

def get_case_data_list(file_name: str) -> list:
    """
    读取文本用例数据
    :param file_name: 文件路径
    :return: list
    """
    with open(file_name, mode="r", encoding="utf-8") as f:
        data_list = f.readlines()
    data_list = [line.strip() for line in data_list]
    return data_list


def read_file_dict(file_name: str) -> dict:
    record_dic = {}
    if '.yaml' in file_name:
        with open(file_name, 'r', encoding='utf-8') as wf:
            record_dic = yaml.safe_load(wf)
    elif '.json' in file_name:
        with open (file_name, 'r') as wf:
            record_dic = json.load (wf)
    else:
        # logger.info(f'file not support:{read_file_dict}')
        pass
    return record_dic

def dump_file(file_name, data) -> int:
    # file_name = os.path.join(file_path, file_name)
    with open(file_name, 'w', encoding='utf-8') as wf:
        yaml.safe_dump(data, wf, default_flow_style=False, allow_unicode=True, sort_keys=False)
    return 0

def dump_json(file_name: str, data: dict) -> int:
    """
    读取文本用例数据
    :param file_name: 文件路径
    :return: list
    """
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)
    return 0

def read_file_str(file_name):
    """
    读取文本用例数据
    :param file_name: 文件路径
    :return: list
    """
    # 打开文件，返回一个文件对象
    with open(file_name, 'r', encoding='gbk') as file:
        # 读取文件的全部内容
        content = file.read()
        # logger.info(content)
    return content

def wrtie_file(file_name, content) -> None:
    # 打开文件，如果文件不存在，会创建文件；'a' 表示追加模式，如果文件已存在，则会在文件末尾追加内容
    with open (file_name, 'w', encoding='utf-8') as file:
        # 追加文本数据
        file.write(content)
    return

def add_string_to_first_line(file_path, new_string):
    try:
        # 以只读模式打开文件并读取所有内容
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # 在内容开头插入新的字符串，并添加换行符
        lines.insert(0, new_string + '\n')

        # 以写入模式打开文件并将更新后的内容写回
        with open(file_path, 'w', encoding='utf-8') as file:
            file.writelines(lines)

        # logger.info(f"成功在文件 {file_path} 的第一行添加字符串。")
    except FileNotFoundError:
        logger.info(f"未找到文件: {file_path}")
    except Exception as e:
        logger.info(f"发生错误: {e}")
    return

def get_file_content_list_remove_empty_line(file_path):
    log_lines = []
    try:
        # 以只读模式打开文件并读取所有内容
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            log_lines = f.readlines()  # 列表形式存储每一行日志，保留换行符
    except FileNotFoundError:
        logger.info(f"未找到文件: {file_path}")
    except Exception as e:
        logger.info(f"发生错误: {e}")
    if log_lines:
        for line in log_lines:
            new_line = line.replace('\n', '').strip()
            # logger.info(f"new_line: {new_line}")
            if new_line == '':
                log_lines.remove(line)
                # logger.info(f"removed_line:")

    # logger.info(f"log_lines:{log_lines}")
    return log_lines

def get_file_content_list(file_path):
    log_lines = []
    try:
        # 以只读模式打开文件并读取所有内容
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            log_lines = f.readlines()  # 列表形式存储每一行日志，保留换行符
    except FileNotFoundError:
        logger.info(f"未找到文件: {file_path}")
    except Exception as e:
        logger.info(f"发生错误: {e}")
    return log_lines

if __name__ == '__main__':
    current_enable = True
    if current_enable:
        data_dict = {}
        data_dict['b'] = 'b'
        data_dict['a'] = 'a'
        file = r'D:/hello.yaml'
        dump_file(file, data_dict)
    else:
        pass