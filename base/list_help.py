# coding=utf-8

import yaml
import json
import os
from utils.logger_util import logger


def get_list_text_line_last_index(input_list, text):
    index = None
    if input_list is None:
        return index

    for idx, line in enumerate(input_list):
        if text in line:
            index = idx
    return index

def get_list_text_line_first_index(input_list, text):
    index = None
    if input_list is None:
        return index

    for idx, line in enumerate(input_list):
        if text in line:
            index = idx
            break
    return index

def get_list_text_line(result, text):
    text_line = ''
    if result is None:
        return text_line

    for item in result:
        if text in item:
            text_line = item
            break
    return text_line

def get_list_strip(result):
    text_lines = []
    if result is None:
        return text_lines

    for item in result:
        item = item.strip('\n')
        item = item.strip()
        if item:
            # logger.info(f'item:{item}')
            text_lines.append(f'{item}')
    return text_lines

def get_list_text_lines(result, text):
    text_lines = []
    if result is None:
        return text_lines
    for item in result:
        value = item.strip('\n')
        value = item.strip()
        if value and text in value:
            text_lines.append(value)
    return text_lines

def is_list_has_target_text(text_list, target_text):
    has_target_text = False
    for item in text_list:
        if target_text in item:
            has_target_text = True
            break
    return has_target_text

def get_list_text_count(result, text):
    text_line = None
    count = 0
    if result is None:
        return count

    for item in result:
        if text in item:
            count = count + 1
    return count

def remove_list_text_with_target_text(input_list, remove_target_text_1, remove_target_text_2):
    new_list = []
    if input_list is None:
        return new_list

    for item in input_list:
        item = item.replace(remove_target_text_1, '').strip()
        item = item.replace(remove_target_text_2, '').strip()
        if item :
            new_list.append(item)
    return new_list

def remove_list_na(input_list, target_str='NA'):
    out_list = []
    if input_list is None:
        return out_list
    for item in input_list:
        if target_str not in str(item) and 'nan' not in str(item) and 'Invalid' not in str(item):
            out_list.append(item)
    return out_list

def remove_list_emptpy(input_list):
    new_list = []
    index = None
    if input_list is None:
        return index
    # logger.info(f'input_list:{input_list}')


    for line in input_list:
        # logger.info(f'xutong:{line}')
        line = line.replace('\n', '')
        # line = line.replace('\t', '')
        new_line = line.strip()
        length = len(new_line)
        # logger.info(f'line:{line}, new_line:{new_line}, length:{length}')
        if length > 0:
            new_list.append(new_line)
    return new_list

def get_list_average(input_list, debug = False):
    output_list = []
    average = None
    total = 0
    if input_list is None:
        return average

    input_list = remove_list_na(input_list, 'nan')

    # logger.info(f"input_list:{input_list}")
    for item in input_list:
        type_str = type(item)
        # logger.info(f"type_str:{type_str}")
        if type(item) is str:
            is_number = is_digital_item(item)
            if is_number:
                item = float(item)
                output_list.append(item)
        if type(item) is int or type(item) is float:
            output_list.append(item)
        if debug:
            logger.info(f"item:{item}")

    # logger.info(f"output_list:{output_list}")
    if len(output_list):
        average = sum(output_list) / len(output_list)
    return average

def split_list(lst, num):
    length = len(lst)
    part_length = length // num  # 计算每一部分的长度
    remainder = length % num  # 计算余数
    parts = []
    start = 0
    for i in range(num):
        if i < remainder:  # 对于余数部分，将长度加 1
            end = start + part_length + 1
        else:
            end = start + part_length
        parts.append(lst[start:end])  # 截取列表的一部分添加到结果中
        start = end
    return parts

def get_list_equal_count(result, text):
    text_line = None
    count = 0
    if result is None:
        return count

    for item in result:
        if text == item:
            count = count + 1
    return count

def get_list_lower_index(input_list, bench_mark):
    target_index = None
    for idx, item in enumerate(input_list):
        if float(item) < bench_mark:
            target_index = idx
            break
    return target_index

def get_list_lower_index_list(input_list, bench_mark):
    target_index_list = []
    for idx, item in enumerate(input_list):
        if float(item) < bench_mark:
            target_index_list.append(idx)
            break
    return target_index_list

def get_list_lower_equal_index(input_list, bench_mark):
    target_index = None
    for idx, item in enumerate(input_list):
        # logger.info(f"item: {item}")
        if float(item) <= bench_mark:
            target_index = idx
            break
    return target_index

def similarity_ratio(str1, str2):
    return difflib.SequenceMatcher(None, str1, str2).ratio()

def get_match_col_name(head_list, col_name):
    max_ratio = 0
    max_ratio_index = None
    col = None
    for idx, item in enumerate(head_list):
        curr_ratio = similarity_ratio(item, col_name)
        if curr_ratio > max_ratio:
            max_ratio = curr_ratio
            max_ratio_index = idx
    col = head_list[max_ratio_index]
    # logger.info(f'col:{col}')
    return col

if __name__ == '__main__':
    pass