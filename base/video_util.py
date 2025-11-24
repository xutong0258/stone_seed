# coding=utf-8
import os
import sys
import json
import time
import warnings
import platform
import shutil
import datetime
from moviepy.editor import *
import cv2
import matplotlib.pyplot as plt


file_path = os.path.abspath(__file__)
path_dir = os.path.dirname(file_path)
base_name = os.path.basename(path_dir)

while 'se-autotest' not in base_name:
    path_dir = os.path.dirname(path_dir)
    base_name = os.path.basename(path_dir)

sys.path.append(path_dir)

import fileOP
from util import *
from mylogger import *
from common.contants import *

from moviepy.editor import VideoFileClip, concatenate_videoclips


def remove_start_part(input_path=None, output_path=None, start_time=None):
    if not input_path:
        # 输入视频文件的路径
        input_video_path = r"D:\99_TEST_VIDEO\01_stand_jump\full_score\2025_3_10_14_36_49_192.168.2.100_1_1_B_face_9_2.mp4"
        # 输出视频文件的路径
        output_video_path = r"D:\99_TEST_VIDEO\01_stand_jump\full_score\output_video.mp4"
        # 要删除的开始部分的时长（秒）
        start_time_to_remove = 1

    # 调用函数删除视频开始部分
    # remove_start_part(input_video_path, output_video_path, start_time_to_remove)

    # 加载视频文件
    clip = VideoFileClip(input_video_path)
    # 从指定时间开始剪辑视频
    new_clip = clip.subclip(start_time_to_remove)
    # 将剪辑后的视频保存到指定路径
    new_clip.write_videofile(output_video_path, codec="libx265")
    # 关闭剪辑对象，释放资源
    clip.close()
    new_clip.close()
    return


def remove_middle_part(input_video_path, output_video_path, start_time, end_time):
    # 加载视频文件
    clip = VideoFileClip(input_video_path)

    # 分割视频为前半部分和后半部分
    front_clip = clip.subclip(0, start_time)
    back_clip = clip.subclip(end_time)

    # 拼接前半部分和后半部分
    final_clip = concatenate_videoclips([front_clip, back_clip])

    # 保存处理后的视频
    final_clip.write_videofile(output_video_path, codec="libx264")

    # 关闭剪辑对象以释放资源
    clip.close()
    final_clip.close()
    return

# scale=2560:1440
# scale=3840:2160
# ffmpeg -i target.mp4 -vf "scale=2560:1440" -q:v 20 -b:v 2M -c:v libx265 -c:a copy final.mp4
def video_concatenate():
    file_list = []

    file = r'D:\99_TEST_VIDEO\05_rope_skip\fake_led\pre.mp4'

    video = VideoFileClip (file)
    file_list.append (video)

    for index in range(3):
        file = r'D:\99_TEST_VIDEO\05_rope_skip\fake_led\11.mp4'
        video = VideoFileClip (file)
        file_list.append (video)

    final_clip = concatenate_videoclips (file_list)

    final_clip.to_videofile (r"D:\99_TEST_VIDEO\05_rope_skip\fake_led\target.mp4", fps=25, remove_temp=False, codec="libx265")
    return


def draw_skeleton(image_path=None, keypoints=None, output_path=None):

    image = cv2.imread(image_path)

    # 绘制关键点
    for keypoint in keypoints:
        for point in keypoint:
            if point == 0:
                pass
                # print('点可能不在人体框内，或者在画面外')
                # print(image_path)
            else:
                x, y = point
                cv2.circle(image, (int(x), int(y)), 5, (0, 255, 0), -1)  # 绘制绿色圆圈


    # 如果指定了输出路径，保存图片
    if output_path:
        cv2.imwrite(output_path, image)
    return

def draw_point_on_image(image, point):

    # 定义点的坐标
    # point = (100, 100)  # 这里的(100, 100)是点的(x, y)坐标

    # 定义点的颜色（BGR格式）
    color = (0, 255, 0)  # 绿色

    # 定义点的半径
    radius = 10

    # 定义线条的粗细
    thickness = -1  # -1表示填充圆

    # 在图像上画点
    cv2.circle(image, point, radius, color, thickness)
    return

def rope_cfg_check():
    dir = r'D:\11\orgi_test'
    image_path = os.path.join(dir, '1.jpg')
    image = cv2.imread (image_path)

    dir = r'D:\11\orgi_test'
    file = '2560p.json'
    full_file = os.path.join (dir, file)
    hello_dict = fileOP.read_file_dict (full_file)
    # logger.info(f'hello_dict:{hello_dict}')
    item_list = ['']
    point_dict = {}
    for item in range (0, 10):
        diction_key = f'Location{item}'
        diction_tmp = hello_dict[diction_key]
        logger.info (f'diction_tmp:{diction_tmp}')
        ReadyPt1_x = diction_tmp.get('ReadyPt1_x', 0)
        ReadyPt1_y = diction_tmp.get ('ReadyPt1_y', 0)
        point = (ReadyPt1_x, ReadyPt1_y)
        draw_point_on_image(image, point)

        ReadyPt1_x = diction_tmp.get('ReadyPt2_x', 0)
        ReadyPt1_y = diction_tmp.get ('ReadyPt2_y', 0)
        point = (ReadyPt1_x, ReadyPt1_y)
        draw_point_on_image(image, point)

    # 保存修改后的图像
    output_path = r'D:\2.jpg'
    cv2.imwrite(output_path, image)
    return


def get_video_duration_ffprobe(video_path):
    command = [
        'ffprobe',
        '-v', 'error',
        '-show_entries', 'format=duration',
        '-of', 'default=noprint_wrappers=1:nokey=1',
        video_path
    ]
    result = 0
    try:
        result = subprocess.check_output(command).decode('utf-8').strip()
    except Exception as ex:
        print(f'Exception:{ex}')
        result = 0
    finally:
        pass
    return float(result)


def get_video_resolution(video_path):
    # video_path = r'D:\test\concat.mp4'
    # 打开视频文件
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        raise ValueError("无法打开视频文件，请检查文件路径是否正确。")
    # 获取视频的宽度
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 获取视频的高度
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 释放视频文件
    cap.release()
    logger.info (f'width:{width}, height:{height}')
    return width, height

if __name__ == '__main__':
    # video_concatenate()
    # rope_cfg_check()
    pass
