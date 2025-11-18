# coding=utf-8

import os
import sys
import logging
import time
import datetime

# file = os.path.abspath(__file__)
path_dir = os.path.dirname(__file__)

split_list = path_dir.split('\\')

LOG_DIR = os.path.join(split_list[0], f"\\auto_test_log")
# print(f'LOG_DIR:{LOG_DIR}')

if not os.path.exists(LOG_DIR):
    # print(f'os.mkdir:{LOG_DIR}')
    os.mkdir(LOG_DIR)


time_stamp = datetime.datetime.now().strftime("%Y%m%d%H%M")
filename = f'test_{time_stamp}.log'

# 获取日志文件的绝对路径
log_file = os.path.join(LOG_DIR, filename)

formatter2 = logging.Formatter(
    '[%(asctime)s]'
    '%(filename)s'
    '[Line:%(lineno)d]: '
    '%(message)s'
)

CH = logging.StreamHandler()
CH.setLevel(logging.DEBUG)
CH.setFormatter(formatter2)

global current_enable
current_enable = False

if current_enable:
    LOG = logging.getLogger(__file__)
    LOG.setLevel (logging.DEBUG)
    LOG.addHandler (CH)

_format =('[%(asctime)s][%(filename)s][%(funcName)s][%(lineno)s]'
' %(levelname)s: %(message)s')

# for differnt module, different log

def init_logger(loggername, file=None):
    logger = logging.getLogger(loggername)
    logger.setLevel(level=logging.DEBUG)
    if not logger.handlers and file:
        file_handler = logging.FileHandler(file, encoding="utf8")
        file_format = logging.Formatter(_format)
        file_handler.setFormatter(file_format)
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)
        logger.addHandler(CH)
    return logger

print(f'log_file:{log_file}')
logger = init_logger(__file__, log_file)
# logger.info('hello')


if __name__ == '__main__':
    logger.info(f'result:')

