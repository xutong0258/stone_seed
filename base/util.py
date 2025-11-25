# coding=utf-8

import json
import os
import shutil
import sys
import logging
import time
import datetime
import re
import subprocess

# file = os.path.abspath(__file__)
path_dir = os.path.dirname(__file__)


def is_digital_item(cell_item):
    number_list = ['0','1','2','3','4','5','6','7','8','9']
    is_number = True
    for item in cell_item:
        # logger.info(f"item:{item}")
        if item not in number_list:
            is_number = False
            break
    # logger.info(f"is_number:{is_number}")
    return is_number

if __name__ == '__main__':
    pass
