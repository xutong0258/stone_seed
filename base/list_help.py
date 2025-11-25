# coding=utf-8

import yaml
import json
import os
from utils.logger_util import *


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

if __name__ == '__main__':
    pass