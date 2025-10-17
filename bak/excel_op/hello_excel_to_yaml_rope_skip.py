import pandas as pd
import yaml
import io
import os
import sys
import platform

from base import fileOP
from base.util import *

file_name = os.path.abspath(__file__)
path_dir = os.path.dirname(file_name)


def excel_to_yaml(excel_file_path, yaml_file_path):
    # 读取 Excel 文件
    df = pd.read_excel(excel_file_path)

    # 将 DataFrame 转换为字典列表
    data = df.to_dict(orient='records')

    logger.info(f'data:{data}')
    # 重新组织数据，以 Video_Filename 为键
    reorganized_data = {}
    for item in data:
        video_filename = item['Video_Filename']
        location = item['location']
        if video_filename not in reorganized_data:
            reorganized_data[video_filename] = {}
        reorganized_data[video_filename][location] = {
            'Fake_Jump_Times': item['Fake_Jump_Times'],
            'Number': item['Number']
        }

    # data to yaml
    fileOP.dump_file(yaml_file_path, reorganized_data)


# 示例用法
excel_file = r'D:\00_stone_project\data\output.xlsx'
yaml_file = 'example.yaml'
excel_to_yaml(excel_file, yaml_file)
