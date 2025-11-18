# coding=utf-8

import json
import os
import shutil
import sys
import time
import datetime
import subprocess
from base.logger import logger

# file = os.path.abspath(__file__)
path_dir = os.path.dirname(__file__)

# os.system
def cmd_excute(cmd, logger=None, outfile=None, errfile=None):
    if outfile is None and errfile is None:
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()
        # print(stdout.decode())
        # result = stdout.decode('utf-8').strip('\r\n')
        result = stdout
        errors = stderr
        return_code = process.returncode
        msg = result if not stderr else errors
        if logger:
            logger.info(cmd)
            logger.debug(return_code)
            if return_code != 0:
                logger.error(errors)

        return result, errors, return_code
    else:
        f_out = open(outfile, 'w')
        f_err = open(errfile, 'w')
        process = subprocess.Popen(
            cmd,
            shell=True,
            stdout=f_out,
            stderr=f_err)
        output, errors = process.communicate()
        return_code = process.returncode
        if logger:
            logger.info(cmd)
            logger.debug(return_code)
        if return_code != 0:
            logger.error(errors)
        return return_code

if __name__ == '__main__':
    cmd = f'echo "hello world"'
    result, errors, return_code = cmd_excute(cmd)
    logger.info(f'result:{result}')
    logger.info(f'errors:{errors}')
    logger.info(f'return_code:{return_code}')
