"""
命令行版本的日志分析工具
用法: python pipeline_cmd.py <dump_path>
"""

import sys
import argparse
from pathlib import Path
from urllib.parse import quote_plus


from logger_util import logger

def parse_arguments():
    """
    解析命令行参数

    :return: 解析后的参数
    """
    parser = argparse.ArgumentParser(
        description="BSOD 日志分析工具 - 分析内存转储文件并生成根因分析",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python pipeline_cmd.py D:\\dumps\\MEMORY.DMP
  python pipeline_cmd.py "C:\\Program Files\\dumps\\crash.dmp"
        """,
    )

    parser.add_argument(
        "dump_path", type=str, help="内存转储文件 (MEMORY.DMP) 的完整路径"
    )

    parser.add_argument(
        "--bsod-id",
        type=str,
        default="BSOD_ROOT",
        help="BSOD 分析模板 ID (默认: BSOD_ROOT)",
    )

    return parser.parse_args()


def main():
    """
    主函数

    :return: 退出码 (0=成功, 1=失败)
    """
    try:
        # 1. 解析命令行参数
        args = parse_arguments()

        logger.info("=" * 60)
        logger.info("BSOD 日志分析工具启动")
        logger.info("=" * 60)
        return 0

    except FileNotFoundError as e:
        logger.error(str(e))
        return 1

    except ValueError as e:
        logger.error(str(e))
        return 1

    except KeyboardInterrupt:
        logger.warning("\n用户中断执行")
        return 130

    except Exception as e:
        logger.error(f"执行失败: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    logger.info("BSOD 日志分析工具启动")
    """
    uv run python -m app.services.log_analyze.pipeline_cmd 'D:\BaiduNetdiskDownload\开发样本_0x9f_4_IRP_Intel WLAN\MEMORY.DMP'
    """
    exit_code = main()
    sys.exit(exit_code)
