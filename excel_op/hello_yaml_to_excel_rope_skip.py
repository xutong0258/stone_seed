import yaml
import pandas as pd

# 示例 YAML 数据
yaml_data = """
2023_10_25_14_57_4_192.168.2.107_5_face_9_-1.mp4:
  '1':
    fakeJumpTimes: 0
    number: 187.0
  '10':
    fakeJumpTimes: 80
    number: 191.0
2023_10_12_11_24_13_192.168.2.203_5_face_9_-11.mp4:
  '1':
    fakeJumpTimes: 8
    number: 116.0
  '10':
    fakeJumpTimes: 13
    number: 95.0
  '2':
    fakeJumpTimes: 0
    number: 172.0
  '3':
    fakeJumpTimes: 0
    number: 197.0
"""

# 解析 YAML 数据
parsed_data = yaml.safe_load(yaml_data)

# 提取数据并转换为适合 DataFrame 的格式
video_filename_list = list(parsed_data.keys())
data_list = []
for video_filename in video_filename_list:
    for key, values in parsed_data[video_filename].items():
        row = {
            'Video_Filename': video_filename,
            'location': key,
            'Fake_Jump_Times': values['fakeJumpTimes'],
            'Number': values['number']
        }
        data_list.append(row)

# 创建 DataFrame
df = pd.DataFrame(data_list)

# 保存为 Excel 文件
excel_file = 'output.xlsx'
df.to_excel(excel_file, index=False)

print(f"数据已成功保存到 {excel_file}")
