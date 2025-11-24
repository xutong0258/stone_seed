import os
import sys

file_path = os.path.abspath(__file__)
path_dir = os.path.dirname(file_path)

root_dir = os.path.join(path_dir, '../')
sys.path.append(root_dir)


from base.contants import *
from base.fileOP import *

path_dir = os.path.dirname(__file__)

def check_rule_2(config_dict, *args, **kwargs):
    parent_dir = kwargs.get('parent_dir', 'Unknown')
    logger.info(f'parent_dir: {parent_dir}')

    fail_dir = kwargs.get('fail_dir', None)
    pass_dir = kwargs.get('pass_dir', None)

    if parent_dir is not None:
        fail_dir = os.path.join(parent_dir, 'fail')
        pass_dir = os.path.join(parent_dir, 'pass')
    return

if __name__ == '__main__':
    parent_dir = r'D:\0_intelcpu_case_1112\cpu Sample_rule1'
    # check_rule_1(parent_dir=parent_dir, fail_dir=None, pass_dir=None)

    file = os.path.join(CONFIG_PATH, 'intel_check_rule.yaml')
    intel_rule_dict = read_file_dict(file)
    # logger.info(f'intel_rule_dict={intel_rule_dict}')

    check_rule_2(intel_rule_dict, parent_dir=parent_dir, fail_dir=None, pass_dir=None)
    pass

