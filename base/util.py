# coding=utf-8

import json
import os
import shutil
import sys
import logging
import time
import datetime
import re
from base import fileOP
import cv2
import subprocess

# file = os.path.abspath(__file__)
path_dir = os.path.dirname(__file__)


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

if __name__ == '__main__':
    pass
