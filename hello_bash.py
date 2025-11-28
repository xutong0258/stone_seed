# coding=utf-8
"""
图谱主入口
基于知识图谱的性能问题诊断系统
"""

import os
import sys

# 添加项目根目录到路径
project_root = os.path.dirname(__file__)
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from utils.logger_util import logger

def run_graph_diagnosis(parent_dir):
    logger.error(f"parent_dir: {parent_dir}")
    return

if __name__ == '__main__':
    # 示例用法
    # 方式1：直接指定目录
    parent_dir = r'.\case\case\0_intelcpu_case_1112\CPU_prochot_rule2'

    # 方式2：从命令行参数获取
    if len(sys.argv) > 1:
        parent_dir = sys.argv[1]

    if not os.path.exists(parent_dir):
        logger.error(f"目录不存在: {parent_dir}")
        logger.info("用法: python main_graph.py <日志目录>")
        sys.exit(1)

    run_graph_diagnosis(parent_dir)