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
    pass
