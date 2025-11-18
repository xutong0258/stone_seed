# coding=utf-8
import os
import sys

file_path = os.path.abspath(__file__)
path_dir = os.path.dirname(file_path)
base_name = os.path.basename(path_dir)

sys.path.append(path_dir)


windbgx_path = r"C:\Users\15319\AppData\Local\Microsoft\WindowsApps\WinDbgX.exe"
kdX86_path = r"C:\Users\15319\AppData\Local\Microsoft\WindowsApps\kdX86.exe"
SYMBOL_PATH = "SRV*C:\Symbols*http://msdl.microsoft.com/download/symbols"

command_sleep_map = {
    'analyze': 10,
    'storadapter': 6,
    'devstack': 15,
    'powertriage': 40, # 30
    'amli lc': 15,
    'locks': 15,
    '!WHEA': 10,
    'errrec': 10,
    'irp': 10,
    'usb_tree': 25,
    'thread': 5,
    'running': 5,
    'amli r': 15,
}