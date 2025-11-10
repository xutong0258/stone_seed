# coding=utf-8
import os
import signal
import subprocess
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

file_path = os.path.abspath(__file__)
path_dir = os.path.dirname(file_path)
base_name = os.path.basename(path_dir)

while 'se-autotest' not in base_name:
    path_dir = os.path.dirname(path_dir)
    base_name = os.path.basename(path_dir)

sys.path.append(path_dir)

import fileOP
from mylogger import *
from common.contants import *


def start_fake_camera_simple(video_path, whole_rtsp=None, is_loop=True):
    if ENV == 'Windows' and ('r\'' in video_path or 'r"' in video_path):
        video_path = eval(video_path)

    if os.path.exists(video_path):
        ffmpeg = Ffmpeg(video_path=video_path, rtsp_url=whole_rtsp, is_loop=is_loop)
        ffmpeg.start()
    else:
        raise ValueError(f'File not exist:{video_path}')
    return ffmpeg

def start_fake_camera_simple_dir(video_path_dir, whole_rtsp):
    # 开启进程执行ffmpeg命令，一直推流
    while True:
        total_list = list ()
        file_list = os.listdir (video_path_dir)
        for item in file_list:
            file = os.path.join (video_path_dir, item)
            total_list.append (file)

        for file_name in total_list:
            if '.mp4' not in file_name or '.ts' not in file_name:
                continue


            ffmpeg = Ffmpeg (video_path=file_name, rtsp_url=whole_rtsp, is_loop=True)
            ffmpeg.start ()

            timeout = get_video_duration_ffprobe (file_name)
            time.sleep (timeout)
    return

def start_fake_camera_multi_dir(video_path_dir_list, whole_rtsp):
    # 开启进程执行ffmpeg命令，一直推流
    while True:
        total_list = list ()
        print(f'video_path_dir_list:{video_path_dir_list}')
        for dir in video_path_dir_list:
            print (f'dir:{dir}')
            file_list = os.listdir (dir)
            for item in file_list:
                file = os.path.join (dir, item)
                total_list.append (file)

        for file_name in total_list:
            ffmpeg = Ffmpeg (video_path=file_name, rtsp_url=whole_rtsp, is_loop=True)
            ffmpeg.start ()

            timeout = get_video_duration_ffprobe (file_name)
            time.sleep (timeout)
    return

def push_multi_pro_sit_up_video():
    whole_rtsp = f'rtsp://{PUSH_VIDEO_SERVER}:8554/live304'
    if ENV == 'Linux':
        video_path_dir = '/home/yskj/data/video/CPP_Stress/03_multi_pro_mix_sit_up'
    else:
        video_path_dir = r"D:\99_TEST_VIDEO\CPP_Stress\03_multi_pro_mix_sit_up"

    start_fake_camera_simple_dir(video_path_dir, whole_rtsp=whole_rtsp)
    return

def push_multi_sit_forward_video():
    whole_rtsp = f'rtsp://{PUSH_VIDEO_SERVER}:8554/live304'
    if ENV == 'Linux':
        video_path_dir_list = list()
        video_path_dir_list.append ('/home/yskj/data/video/CPP_Stress/03_multi_sit_forward_p1')
        video_path_dir_list.append('/home/yskj/data/video/CPP_Stress/03_sitforward/A')
    else:
        video_path_dir_list = list()
        video_path_dir_list.append(r"D:\99_TEST_VIDEO\CPP_Stress\03_multi_sit_forward_p1")
        video_path_dir_list.append (r"D:\99_TEST_VIDEO\CPP_Stress\03_sitforward\A")

    start_fake_camera_multi_dir(video_path_dir_list, whole_rtsp=whole_rtsp)
    return

def push_rope_skip_video():
    whole_rtsp = f'rtsp://{PUSH_VIDEO_SERVER}:8554/live501'
    if ENV == 'Linux':
        video_path_dir = '/home/yskj/data/video/CPP_Stress/06_rope_skip/count_test/bak'
    else:
        video_path_dir = r"D:\99_TEST_VIDEO\05_rope_skip\fake_led\final"

    start_fake_camera_simple_dir(video_path_dir, whole_rtsp=whole_rtsp)
    return

class Ffmpeg:
    def __init__(self, video_path, rtsp_url, is_loop=True):
        # rtsp://192.168.2.14:8554/live6204
        if not rtsp_url:
            raise ValueError (f'rtsp_url wrong:{rtsp_url}')

        self.video_path = video_path.replace('\\', '/')
        self.rtsp_url = rtsp_url
        self.process = None
        self.is_loop = is_loop
        return

    def start(self):
        my_log.info("播放视频的地址video_path：{}".format(self.video_path))
        my_log.info("rtsp服务的地址：{}".format(self.rtsp_url))
        # command = f'ffmpeg -re -stream_loop -1 -i {self.video_path}
        # -c copy -f rtsp -rtsp_transport tcp {self.rtsp_url}'
        command = f'ffmpeg -re '
        if self.is_loop:
            command = command + f' -stream_loop -1 '
        command = command + f' -i {self.video_path} '
        # command = command + f' -c copy -an -f rtsp -rtsp_transport tcp {self.rtsp_url}'
        # -codec copy -tune:v zerolatency -an -f rtsp -rtsp_transport tcp
        command = command + f' -r 25 -codec copy -tune:v zerolatency -an -f rtsp -rtsp_transport tcp {self.rtsp_url}'
        my_log.info("执行command的命令：{}".format(command))
        self.process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
        return

    def stop(self):
        if self.process is not None:
            self.process.send_signal(signal.SIGTERM)
            time.sleep(1)
            self.process = None

    def push_video_thread(self):
        p_cnt = 1
        pool_list = []
        thread_pool = ThreadPoolExecutor (p_cnt)
        for index in range (0, p_cnt):
            pool_list.append (thread_pool.submit())
        for fu in as_completed (pool_list):
            res = fu.result ()

        time.sleep (5)
        p_cnt = 1
        pool_list = []
        thread_pool = ThreadPoolExecutor (p_cnt)
        for index in range (0, p_cnt):
            # pool_list.append (thread_pool.submit (start_fake_camera_simple, '211'))
            pass
        for fu in as_completed (pool_list):
            res = fu.result ()
        return


def push_multi_sit_up():
    # video = r"D:\99_TEST_VIDEO\CPP_Stress\02_multi_situp\101\2024_11_5_15_2_26_192.168.2.101_1_3_F_.mp4"
    # start_fake_camera_simple(video, )
    if ENV == 'Linux':
        video_path_dir = "/home/yskj/data/video/CPP_Stress/02_multi_situp"
    else:
        video_path_dir = r"D:\99_TEST_VIDEO\CPP_Stress\02_multi_situp"

    start_fake_camera_simple_dir(video_path_dir, whole_rtsp=f'rtsp://{PUSH_VIDEO_SERVER}:8554/live304')
    return

def push_sit_up_video():
    video_path = r"D:\99_TEST_VIDEO\03_sit_up\sanity\11.mp4"
    rtsp_url_1 = f'rtsp://{PUSH_VIDEO_SERVER}:8554/live301'

    start_fake_camera_simple(video_path, rtsp_url_1)
    return

def push_50M_video():
    video_path_1 = r"D:\99_TEST_VIDEO\06_run_50m\finish_same_time\2_同时过线_start.mp4"
    rtsp_url_1 = f'rtsp://{PUSH_VIDEO_SERVER}:8554/live6204'

    video_path_2 = r"D:\99_TEST_VIDEO\06_run_50m\finish_same_time\2_同时过线_end.mp4"
    rtsp_url_2 = f'rtsp://{PUSH_VIDEO_SERVER}:8554/live6207'

    start_fake_camera_simple(video_path_1, rtsp_url_1)
    start_fake_camera_simple (video_path_2, rtsp_url_2)
    return

def push_rope_skip():
    if ENV == 'Linux':
        video_path_dir = "/home/yskj/data/video/05_rope_skip/test/Zhejiang_jiaxingshiyan/final_test/2023_10_11_14_17_25_192.168.2.203_5_face_1_2.mp4"
    else:
        video_path_dir = r"D:\99_TEST_VIDEO\05_rope_skip\test\Zhejiang_jiaxingshiyan\final_test\2023_10_11_14_17_25_192.168.2.203_5_face_1_2.mp4"

    start_fake_camera_simple(video_path_dir, whole_rtsp=f'rtsp://{PUSH_VIDEO_SERVER}:8554/live511')
    return

def push_800M_video():
    video_path_1 = r"D:\99_TEST_VIDEO\07_800_run\800_run_001\start.mp4"
    rtsp_url_1 = f'rtsp://{PUSH_VIDEO_SERVER}:8554/live700'
    start_fake_camera_simple (video_path_1, rtsp_url_1)

    video_path_4 = r"D:\99_TEST_VIDEO\07_800_run\800_run_001\over_son.mp4"
    rtsp_url_4 = f'rtsp://{PUSH_VIDEO_SERVER}:8554/live710/Streaming/Channels/3'
    start_fake_camera_simple (video_path_4, rtsp_url_4)

    video_path_3 = r"D:\99_TEST_VIDEO\07_800_run\72_man\2023_11_22_15_18_44_7_face_7_-2.mp4"
    rtsp_url_3 = f'rtsp://{PUSH_VIDEO_SERVER}:8554/live710'

    start_fake_camera_simple (video_path_3, rtsp_url_3)
    return

def push_stand_jump():
    if ENV == 'Linux':
        video_file = "/home/yskj/data/video/01_stand_jump/sanity/stand_jump_001_201.mp4"
    else:
        video_file = r"D:\99_TEST_VIDEO\01_stand_jump\full_score_260\hello.mp4"

    start_fake_camera_simple(video_file, whole_rtsp=f'rtsp://{PUSH_VIDEO_SERVER}:8554/live101')
    return

def push_volley_ball_video():
    if ENV == 'Linux':
        video_file = "/home/yskj/data/video"
    else:
        video_file = r"C:\Users\yskj\Downloads\12.mp4"

    start_fake_camera_simple(video_file, whole_rtsp=f'rtsp://{PUSH_VIDEO_SERVER}:8554/live11')
    return

def push_foot_ball_video():
    if ENV == 'Linux':
        video_file = "/home/yskj/data/video"
    else:
        video_file = r"D:\99_TEST_VIDEO\12_foot_ball\sanity\start\11.mp4"

    start_fake_camera_simple(video_file, whole_rtsp=f'rtsp://{PUSH_VIDEO_SERVER}:8554/live1201')

    if ENV == 'Linux':
        video_file = "/home/yskj/data/video"
    else:
        video_file = r"D:\99_TEST_VIDEO\12_foot_ball\sanity\over\11.mp4"

    start_fake_camera_simple(video_file, whole_rtsp=f'rtsp://{PUSH_VIDEO_SERVER}:8554/live1202')
    return

def push_one_video():
    if ENV == 'Linux':
        video_file = "/home/yskj/data/video"
    else:
        video_file = r"D:\99_TEST_VIDEO\05_rope_skip\fake_led\final\target.mp4"

    start_fake_camera_simple(video_file, whole_rtsp=f'rtsp://{PUSH_VIDEO_SERVER}:8554/live501')
    return

def push_solid_ball_video():
    if ENV == 'Linux':
        video_file = "/home/yskj/data/video"
    else:
        video_file = r'D:\99_TEST_VIDEO\09_solid_ball\sanity\start_1\sanity_score_3_2.mp4'

    start_fake_camera_simple(video_file, whole_rtsp=f'rtsp://{PUSH_VIDEO_SERVER}:8554/live161')

    if ENV == 'Linux':
        video_file = "/home/yskj/data/video"
    else:
        video_file = r'D:\99_TEST_VIDEO\09_solid_ball\sanity\over\sanity_score_3_2.mp4'

    start_fake_camera_simple(video_file, whole_rtsp=f'rtsp://{PUSH_VIDEO_SERVER}:8554/live211')
    return

if __name__ == '__main__':
    # push_one_video()
    # push_volid_ball()
    # push_stand_jump()
    # push_50M_video()
    # push_800M_video()
    # push_sit_up_video()
    # push_pull_up_video()
    pass
