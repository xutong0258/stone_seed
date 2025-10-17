# coding=utf-8
import os
import sys
import platform
import yaml
import pandas as pd

from base.util import *

file_name = os.path.abspath(__file__)
path_dir = os.path.dirname(file_name)


# 读取 Excel 文件
file = r'D:\00_stone_project\data\视频测试集.xlsx'
excel_file = pd.ExcelFile(file)

# 获取指定工作表中的数据
df = excel_file.parse('stand_jump')
logger.info(f'df:{df}')

# 将数据转换为字典格式
data = df.to_dict(orient='records')
logger.info(f'data:{data}')

which_type = type(data)
logger.info(f'which_type:{which_type}')

data = str(data).replace('\'视频名称\': ', '')
data = data.replace(', \'真实成绩/厘米\'', '')

logger.info(f'data:{data}')

data = eval(data)
logger.info(f'data:{data}')

final_dict = {}
for item_dict in data:
    for key, value in item_dict.items():
        final_dict.update({key: f'{value}'})

logger.info(f'final_dict:{final_dict}')

# 将字典数据转换为 YAML 格式
yaml_data = yaml.dump(final_dict, allow_unicode=True)

# 将 YAML 数据写入文件
yaml_file_path = os.path.join(path_dir, 'hello.yaml')
with open(yaml_file_path, 'w', encoding='utf-8') as file:
    file.write(yaml_data)