# coding=utf-8

import json
import os
import shutil
import sys
import logging
import time
import datetime
import re
import cv2
import subprocess
import pandas as pd
import numpy as np
from base.logger import *
import difflib

# file = os.path.abspath(__file__)
path_dir = os.path.dirname(__file__)


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

def remove_list_na(input_list, target_str='NA'):
    out_list = []
    if input_list is None:
        return out_list
    for item in input_list:
        if target_str not in str(item) and 'nan' not in str(item) and 'Invalid' not in str(item):
            out_list.append(item)
    return out_list


def get_list_text_count(result, text):
    text = text.lower()

    text_line = None
    count = 0
    if result is None:
        return count

    data_list = remove_list_na(result, target_str='nan')
    # logger.info(f"data_list: {data_list}")

    for item in data_list:
        item = item.lower()
        # logger.info(f'item:{item}')
        if item and text in item:
            count = count + 1
    return count

def get_list_equal_count(result, text):
    text_line = None
    count = 0
    if result is None:
        return count

    for item in result:
        if text == item:
            count = count + 1
    return count

def get_list_lower_than_stand_average(input_list, stand, debug = False):
    output_list = []
    average = None
    total = 0
    if input_list is None:
        return average

    for item in input_list:
        if item < stand:
            output_list.append(item)
            if debug:
                logger.info(f"item:{item}")
    if len(output_list):
        average = sum(output_list) / len(output_list)
    return average

def is_digital_item(cell_item):
    number_list = ['0','1','2','3','4','5','6','7','8','9']
    is_number = False
    for item in cell_item:
        # logger.info(f"item:{item}")
        if item in number_list:
            is_number = True
            break
    # logger.info(f"is_number:{is_number}")
    return is_number

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


def is_col_data_all_same_with_target(col_data, target_str):
    is_match_target = False
    for item in col_data:
        if target_str in item.strip():
            is_match_target = True
        if target_str not in item.strip():
            is_match_target = False
            break
    return is_match_target

def is_col_data_all_match_range(col_data, target_min, target_max):
    is_all_match = False
    for item in col_data:
        item = float(item.strip())
        if target_min<=item<=target_max:
            is_all_match = True
        if item>target_max or item<target_min:
            is_all_match = False
            break
    return is_all_match

def is_col_data_has_data_match_range(col_data, target_min, target_max):
    has_match = False
    for item in col_data:
        if target_min<=item<=target_max:
            has_match = True
            break
        if item>target_max or item<target_min:
            has_match = False

    return has_match

def is_two_list_delta_larger_than_threshold(col_fail, col_pass, threshold, df_fail):
    is_larger_than_threshold = False

    df_fail['deviation_%'] = calculate_deviation(col_fail, col_pass, base='col_pass')

    df_fail['exceed_threshold'] = df_fail['deviation_%'] > threshold
    # logger.info(f'df_fail:{df_fail}')

    count = get_list_equal_count(df_fail['exceed_threshold'], True)
    if count:
        is_larger_than_threshold = True
    return is_larger_than_threshold

def is_two_col_data_delta_larger_than_threshold(col_1_data, col_2_data, threshold):
    is_delta_larger_than_stand = False
    if col_1_data is not None and col_2_data is not None:
        col_1_data = remove_list_na(col_1_data, target_str='nan')
        col_2_data = remove_list_na(col_2_data, target_str='nan')

        average_1 = get_list_average(col_1_data, False)
        average_2 = get_list_average(col_2_data, False)
        delta = abs(average_1 - average_2)
        logger.info(f'delta:{delta}')
        logger.info(f'threshold:{threshold}')
        if delta >= threshold:
            is_delta_larger_than_stand = True
    return is_delta_larger_than_stand

def is_two_data_delta_larger_than_threshold(data_1, data_2, threshold):
    is_delta_larger_than_stand = False
    # logger.info(f'data_1:{data_1}, data_2:{data_2}')

    if data_1 is None or data_2 is None:
        return is_delta_larger_than_stand

    delta = abs(data_1 - data_2)
    # logger.info(f'delta:{delta}')
    delta_ratio = delta/data_1
    # logger.info(f'delta_ratio:{delta_ratio}')
    if delta_ratio > threshold:
        is_delta_larger_than_stand = True
    return is_delta_larger_than_stand

def is_two_col_same(col_fail, col_pass):
    is_two_coloum_same = True

    for idx, value in enumerate(col_fail):
        if value != col_pass[idx]:
            is_two_coloum_same = False
            break

    return is_two_coloum_same

def get_list_text_line_first_index(input_list, text):
    index = None
    if input_list is None:
        return index

    for idx, line in enumerate(input_list):
        if text in line:
            index = idx
            break
    return index

def get_list_text_line_last_index(input_list, text):
    index = None
    if input_list is None:
        return index

    for idx, line in enumerate(input_list):
        if text in line:
            index = idx
    return index

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


if __name__ == '__main__':
    is_digital_item('170')
    pass
