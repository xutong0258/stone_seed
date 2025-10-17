# coding=utf-8
import os
import sys
import time
import platform


class Test_Sun_Run_001():
    def test_run(self):
        aa = 10
        bb = 20
        cc = aa + bb
        if cc == 30:
            print('hello A')
        else:
            print('hello B')
        return

if __name__ == '__main__':
    obj = Test_Sun_Run_001()
    obj.test_run()