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


def replace_file():
    wait_str = ''
    target_str = ''
    current_dir = r'D:\00_stone_project-237\0_17_stress_cases'
    target_dirs = os.listdir(current_dir)
    final_list = []
    for item in target_dirs:
        path = os.path.join(current_dir, item)
        command = f"cd {path} && sed -i 's/{wait_str}/{target_str}/g' *.yaml"
        cmd_excute(command)
    return

def clean_file():
    C1_Time = datetime.datetime.now ()
    logger.info(f'curreent:{C1_Time}')
    time_stamp = datetime.datetime.now ().strftime ("%Y-%m-%d %H:%M:%S")
    logger.info(f'time_stamp:{time_stamp}')

    # current_dir = os.getcwd()
    for root, dirs, files in os.walk(path_dir):
        for file in files:
            if '.mp4' not in file:
                continue
            file = os.path.join(root, file)

            c2_Time = os.path.getmtime(file)
            c2_Time = datetime.datetime.fromtimestamp(c2_Time)
            delta = C1_Time.__sub__ (c2_Time)
            logger.info(f'delta.days:{delta.days}')
            if delta.days > 5:
                logger.info (f"remove file:{file} delta.days:{delta.days}")
                cmd = f'sudo rm -rf {file}'
                cmd_excute(file)
    return

def copy_file_shutil():
    C1_Time = datetime.datetime.now ()
    logger.info(f'curreent:{C1_Time}')
    time_stamp = datetime.datetime.now ().strftime ("%Y-%m-%d %H:%M:%S")
    logger.info(f'time_stamp:{time_stamp}')

    # current_dir = os.getcwd()
    for root, dirs, files in os.walk(path_dir):
        for file in files:
            if '203' in file:
                dest_file = os.path.join(path_dir, '../total', file)
                source_file = os.path.join(root, file)
                shutil.copyfile(source_file, dest_file)

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

def change_file_name():
    dir = r'D:\0_慧务农\发票\bak\11'
    # /home/yskj/data/sport-ci/conf
    # dir = r'/home/yskj/data/sport-ci/conf'
    tmp_list = os.listdir (dir)
    for item in tmp_list:
        full_path = os.path.join(dir, item)
        new_path = full_path.replace('.pdf', '_33.pdf')
        command = f'mv {full_path} {new_path}'
        # cmd_excute(command, logger)
        os.rename(full_path, new_path)
    return

def delete_folder(folder_path):
    try:
        # 检查文件夹是否存在
        if not os.path.exists(folder_path):
            logger.info(f"错误: 文件夹 '{folder_path}' 不存在")
            return

        # 检查是否是文件夹
        if not os.path.isdir(folder_path):
            logger.info(f"错误: '{folder_path}' 不是一个文件夹")
            return

        # 删除文件夹及其内容
        shutil.rmtree(folder_path)
        logger.info(f"文件夹 '{folder_path}' 已成功删除")

    except PermissionError:
        logger.info(f"错误: 没有权限删除 '{folder_path}'")
    except Exception as e:
        logger.info(f"删除文件夹时发生错误: {str(e)}")

if __name__ == '__main__':
    pass
